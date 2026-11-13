"""Prepare a full-reader EPUB conversion copy from the same frozen inputs as the PDF."""
from collections import Counter
from datetime import datetime, timezone
from hashlib import sha256
import json
from pathlib import Path
import re
import shutil
import sys
import uuid

tools = Path(__file__).resolve().parent
root = tools.parents[1]
prepared = tools / "direct-full"
stage = tools
snapshot = prepared / "source"
frozen_fr = snapshot / "locale/fr"
source_coverage = json.loads((prepared / "SOURCE_COVERAGE.json").read_text(encoding="utf-8"))
graph = source_coverage["reader_graph"]
manifest = root / "provenance/SOURCE_MANIFEST.jsonl"
manifest_rows = [json.loads(line) for line in manifest.read_text(encoding="utf-8-sig").splitlines()]
sha = lambda path: sha256(path.read_bytes()).hexdigest()
assert sha(manifest) == source_coverage["manifest_sha256"]
assert len(manifest_rows) == source_coverage["registered_source_units"] == 722
assert len(graph["loaded_units"]) == source_coverage["potential_printable_units"] == 717
assert len(graph["source_only_drivers"]) == source_coverage["source_only_compilation_drivers"] == 5
assert sha(frozen_fr / "reader.tex") == source_coverage["reader_source_sha256"]
for derived in ("conversion", "overrides"):
    if (stage / derived).exists():
        raise FileExistsError(stage / derived)

loaded_paths = {unit["path"] for unit in graph["loaded_units"]}
source_only_paths = set(graph["source_only_drivers"].values())
assert loaded_paths.isdisjoint(source_only_paths)
assert loaded_paths | source_only_paths == {row["source_path"] for row in manifest_rows}
expected_extra = set(graph["non_manifest_local_tex_inputs"])
inputs = sorted(loaded_paths | expected_extra)
# Only the conversion copy is changed. The PDF snapshot and the editable sources
# retain the original OpenLogic token syntax and exact bytes.
fr = stage / "conversion/source/locale/fr"
pdf_output = re.compile(
    r"reader\.(?:aux|bbl|blg|fls|log|out|pdf|prb|thm|toc)"
    r"|(?:pass-\d+|bibtex-before-\d+)\.log|PDF_BUILD\.json"
)


def ignore_pdf_outputs(directory, names):
    if Path(directory) != frozen_fr:
        return []
    return [name for name in names if pdf_output.fullmatch(name)]


shutil.copytree(snapshot, stage / "conversion/source", ignore=ignore_pdf_outputs)

def capital_token(match):
    article, token, plural = match.groups()
    if article:
        return r"\usetoken{A}{" + token + r"}~\usetoken{" + ("p" if plural else "s") + "}{" + token + "}"
    return r"\usetoken{" + ("P" if plural else "S") + "}{" + token + "}"

# TeX4ht's MathML script handler takes one unbraced token. Keep the
# mandatory argument of each of these one-argument commands with that token.
math_script = re.compile(
    r"(?<!\\)([_^])(\s*\\(Th|Ax|cardfont|mathbb|mathrm|text)\s*\{[^{}\r\n]+\})"
)
deferred_problem = re.compile(r"\\begin\{(prob|probtag)\}.*?\\end\{\1\}", re.S)
transition_table_path = "content/turing-machines/machines-computations/representing-tms.tex"
transition_table = re.compile(
    r"\\\[\n\\centering\n(\\begin\{tabular\}\{lllll\}\n.*?\n\\end\{tabular\})\n\\\]",
    re.S,
)
transforms = {}
for path in inputs:
    frozen = frozen_fr / path
    converted = fr / path
    assert sha(frozen) == sha(converted), path
    text = frozen.read_text(encoding="utf-8")
    assert not re.search(r"!!(?!\^?a?\{)", text), path
    tokens = text.count("!!")
    grouped_scripts = Counter(match[3] for match in math_script.finditer(text))
    induction_exercises = text.count(r"\indcase!")
    problem_tabs = sum(match[0].count("\t") for match in deferred_problem.finditer(text))
    table_displays = 0
    if path == transition_table_path:
        # The table's cell formulas already enter math mode individually.
        # In a display TeX4ht mixes HTML table tags with MathML cells.
        text, table_displays = transition_table.subn(r"\\begin{center}\n\1\n\\end{center}", text)
        assert table_displays == 1, path
    if tokens or grouped_scripts or induction_exercises or problem_tabs or table_displays:
        text = text.replace("!!", r"\OLToken ")
        text = text.replace(r"\indcase!", r"\OLIndcaseExercise")
        if problem_tabs:
            # The deferred writer escapes a tab as literal ^^I. In MathML
            # displays TeX4ht reads its active carets as superscript tokens.
            text = deferred_problem.sub(lambda match: match[0].replace("\t", "  "), text)
        text = math_script.sub(r"\1{\2}", text)
        text = re.sub(r"\\OLToken \^(a?)\{([^}]+)\}(s?)", capital_token, text)
        converted.write_text(text, encoding="utf-8", newline="\n")
        transforms[path] = dict(
            tokens=tokens, grouped_scripts=dict(grouped_scripts),
            induction_exercises=induction_exercises, problem_tabs=problem_tabs,
            table_displays=table_displays,
        )

cfg = (tools / "french-epub.cfg").read_text(encoding="utf-8")
edition_title = "OpenLogic — Édition française"
edition_digest = sha256("".join([
    source_coverage["reader_source_sha256"],
    *(sha(frozen_fr / row["source_path"]) for row in manifest_rows),
]).encode("ascii")).hexdigest()
identifier = "urn:uuid:" + str(uuid.uuid5(
    uuid.NAMESPACE_URL, "https://github.com/KokunoYumeto/OpenLogic-fr/" + edition_digest
))
description = (
    "Édition française du manuel OpenLogic. Ce volume couvre la théorie des ensembles, "
    "la logique propositionnelle et du premier ordre, la théorie des modèles, la calculabilité, "
    "les logiques non classiques et la théorie de la démonstration. "
    "Traduction française et révision éditoriale produites par IA."
)
revision = manifest_rows[0]["source_commit"]
assert all(row["source_commit"] == revision for row in manifest_rows)
source_url = f"https://github.com/OpenLogicProject/OpenLogic/tree/{revision}"
opf_metadata = (
    f"<dc:description>{description}</dc:description>"
    f"<dc:source>{source_url}</dc:source>"
    "<dc:rights>Creative Commons Attribution 4.0 International "
    "(https://creativecommons.org/licenses/by/4.0/)</dc:rights>"
)
fields = {
    r"\title{": r"\title{" + edition_title + "}",
    r"\author{": r"\author{Open Logic Project}",
    r"\Configure{UniqueIdentifier}": r"\Configure{UniqueIdentifier}{" + identifier + "}",
    r"\Configure{OpfMetadata}": r"\Configure{OpfMetadata}{\HCode{" + opf_metadata + "}}",
}
cfg_lines = cfg.splitlines()
for prefix, value in fields.items():
    positions = [i for i, line in enumerate(cfg_lines) if line.startswith(prefix)]
    assert len(positions) == 1, prefix
    cfg_lines[positions[0]] = value
legacy_display_hook = r"\Configure{DisplayProof}{}{}"
for environment in ("prooftree", "defish"):
    legacy_wrapper = rf"\ConfigureEnv{{{environment}}}{{\Picture*{{}}}}{{\EndPicture}}{{}}{{}}"
    assert cfg_lines.count(legacy_wrapper) == 1
    cfg_lines.remove(legacy_wrapper)
assert cfg_lines.count(legacy_display_hook) == 1
cfg_lines[cfg_lines.index(legacy_display_hook)] = (
    r"\Configure{DisplayProof}{\Picture*[Arbre de dérivation]{}}{\EndPicture}"
)
# An active exclamation mark can escape xparse's optional-token test.
# The ordinary French branch prints the same case heading and prompt.
assert cfg_lines.count(r"\EndPreamble") == 1
preamble_end = cfg_lines.index(r"\EndPreamble")
cfg_lines[preamble_end:preamble_end] = [
    r'\Configure{math-xmlns}{ xmlns="http://www.w3.org/1998/Math/MathML"}',
    r"\NewDocumentCommand\OLIndcaseExercise{m m +m}{\indcase{#1}{#2}{exercice.}}",
    r"\input{native-proof-boxes.tex}",
    # The original stmaryrd glyph is a left-right arrow over a horizontal rule.
    r'\renewcommand{\leftrightarroweq}{\HCode{<munder accentunder="true">'
    r'<mo stretchy="false">\string&\#x2194;</mo>'
    r'<mo stretchy="false">\string&\#x2212;</mo></munder>}}',
]
(fr / "french-epub.cfg").write_text("\n".join(cfg_lines) + "\n", encoding="utf-8", newline="\n")
proof_boxes = fr / "native-proof-boxes.tex"
shutil.copy2(tools / proof_boxes.name, proof_boxes)
shutil.copy2(tools / "reader.mk4", fr / "reader.mk4")

tex4ht = tools / "dependencies/tex4ht-texlive/texmf-dist/tex/generic/tex4ht"
bussproofs_hook = tex4ht / "bussproofs.4ht"
proof_hook = bussproofs_hook.read_text(encoding="utf-8")
# The installed Bussproofs DisplayProof takes zero arguments. The legacy
# TeX4ht hooks consume the following token as an argument to DisplayProof.
for wrapper in ("pend", "append"):
    old = rf"\{wrapper}:defI\DisplayProof"
    assert proof_hook.count(old) == 1, wrapper
    proof_hook = proof_hook.replace(old, rf"\{wrapper}:def\DisplayProof")
override = stage / "overrides/bussproofs.4ht"
override.parent.mkdir()
override.write_text(proof_hook, encoding="utf-8", newline="\n")

log_checker = tools / "dependencies/make4ht/make4ht-htlatex.lua"
log_checker_text = log_checker.read_text(encoding="utf-8")
# Only the presence of a file:line:message candidate matters here. The
# original prefix repeats a greedy scan from every position in a log run.
slow_probe = 'content:match("[^:]+%:%d+%:.+")'
assert log_checker_text.count(slow_probe) == 1
log_override = override.with_name(log_checker.name)
log_override.write_text(
    log_checker_text.replace(slow_probe, 'content:match("[^:]%:%d+%:.")'),
    encoding="utf-8", newline="\n",
)

batch_svg = tools / "batch_reader_epub_svg.py"
shutil.copy2(batch_svg, fr / batch_svg.name)
xhtml_normalizer = tools / "normalize_reader_xhtml_before_dom.py"
shutil.copy2(xhtml_normalizer, fr / xhtml_normalizer.name)
postprocessors = [tools / name for name in (
    "repair_epub_generated_navigation.py", "repair_epub_math_markup.py", "inspect_epub.py",
)]
make_utils = log_checker.with_name("mkutils.lua")
make_utils_text = make_utils.read_text(encoding="utf-8")
t4ht_command = '    local command = "t4ht ${t4ht_par} \\"${input}.${ext}\\"" % par'
assert make_utils_text.count(t4ht_command) == 1
after_t4ht = t4ht_command + '\n    log:info("executing: " .. command)\n    execute(command)\n'
assert make_utils_text.count(after_t4ht) == 1
normalize_xhtml = (
    '    assert(os.execute(\'"\' .. python .. \'" -X utf8 normalize_reader_xhtml_before_dom.py\'))\n'
)
make_override = log_override.with_name(make_utils.name)
make_override.write_text(make_utils_text.replace(after_t4ht, (
    '    assert(par.input == "reader", "unexpected full EPUB input")\n'
    '    local python = assert(os.getenv("INTERLANGUAGE_FULL_EPUB_PYTHON"))\n'
    '    assert(os.execute(\'"\' .. python .. \'" -X utf8 batch_reader_epub_svg.py\'))\n'
    '    par.t4ht_par = (par.t4ht_par or "") .. " -p"\n'
    + after_t4ht + normalize_xhtml
)), encoding="utf-8", newline="\n")

mathml_filter = make_utils.parent / "domfilters/make4ht-mathmlfixes.lua"
mathml_filter_text = mathml_filter.read_text(encoding="utf-8")
# The numeric loop has an empty body and raises when find_element_pos()
# returns nil for nodes changed by the HTML parser. It transforms no nodes.
empty_loop = "        for i = pos, 1,-1 do\n        end\n"
assert mathml_filter_text.count(empty_loop) == 1
mathml_override = make_override.parent / "domfilters" / mathml_filter.name
mathml_override.parent.mkdir()
operator_merge = "    fix_operators(el)\n"
assert mathml_filter_text.count(operator_merge) == 1
# The LibreOffice compatibility pass merges the two operands of munder
# into one mtext. EPUB readers need the original MathML operator children.
mathml_override.write_text(
    mathml_filter_text.replace(empty_loop, "").replace(operator_merge, ""),
    encoding="utf-8", newline="\n",
)

section_filter = mathml_filter.with_name("make4ht-sectionid.lua")
section_filter_text = section_filter.read_text(encoding="utf-8")
slug_return = "  return name\nend\n\nlocal function parse_toc_line"
assert section_filter_text.count(slug_return) == 1
section_override = mathml_override.with_name(section_filter.name)
# make4ht's character table can map a heading symbol to an XML control
# character. Encode it before the filter assigns IDs and rewrites links.
escape_controls = (
    '  name = name:gsub("%c", function(c) return string.format("-u%04x-", c:byte()) end)\n'
)
section_override.write_text(
    section_filter_text.replace(slug_return, escape_controls + slug_return),
    encoding="utf-8", newline="\n",
)

units = []
for row in manifest_rows:
    relative = row["source_path"]
    raw = snapshot / relative
    assert sha(raw) == row["source_sha256"], row["unit_id"]
    units.append(dict(
        unit_id=row["unit_id"], path=relative, raw_source_sha256=row["source_sha256"],
        french_snapshot_sha256=sha(frozen_fr / relative), conversion_sha256=sha(fr / relative),
        expected_loaded=relative in loaded_paths, conversion_transform=transforms.get(relative),
    ))
record = dict(
    status="full_reader_epub_sources_prepared", recorded_utc=datetime.now(timezone.utc).isoformat(),
    pdf_source_coverage_sha256=sha(prepared / "SOURCE_COVERAGE.json"),
    upstream_revision=manifest_rows[0]["source_commit"], manifest_sha256=sha(manifest),
    expected_manifest_units_loaded=717, editable_units=722, source_only_drivers=graph["source_only_drivers"],
    expected_load_basis="Reader inputs derived from a prior complete XeLaTeX recorder.",
    reader_snapshot_sha256=sha(frozen_fr / "reader.tex"), reader_conversion_sha256=sha(fr / "reader.tex"),
    metadata_config_sha256=sha(fr / "french-epub.cfg"), edition_title=edition_title, identifier=identifier,
    original_bussproofs_hook_sha256=sha(bussproofs_hook), conversion_bussproofs_hook_sha256=sha(override),
    conversion_native_proof_boxes_sha256=sha(proof_boxes),
    original_make4ht_log_checker_sha256=sha(log_checker), conversion_make4ht_log_checker_sha256=sha(log_override),
    original_make4ht_utils_sha256=sha(make_utils), conversion_make4ht_utils_sha256=sha(make_override),
    conversion_svg_batch_worker_sha256=sha(batch_svg),
    conversion_raw_xhtml_normalizer_sha256=sha(xhtml_normalizer),
    conversion_postprocessor_sha256={script.name:sha(script) for script in postprocessors},
    original_mathml_filter_sha256=sha(mathml_filter), conversion_mathml_filter_sha256=sha(mathml_override),
    original_section_filter_sha256=sha(section_filter), conversion_section_filter_sha256=sha(section_override),
    token_transform_files=len(transforms), token_transform_occurrences=sum(t["tokens"] for t in transforms.values()),
    grouped_math_script_occurrences=sum(sum(t["grouped_scripts"].values()) for t in transforms.values()),
    induction_exercise_occurrences=sum(t["induction_exercises"] for t in transforms.values()),
    deferred_problem_tabs_replaced=sum(t["problem_tabs"] for t in transforms.values()),
    transition_table_displays_rewrapped=sum(t["table_displays"] for t in transforms.values()),
    extra_local_inputs=sorted(expected_extra), units=units,
    epub_content_accepted=False,
)
(stage / "FULL_EPUB_SOURCE_COVERAGE.json").write_text(
    json.dumps(record, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n"
)
print(json.dumps({key: record[key] for key in (
    "status", "editable_units", "expected_manifest_units_loaded", "token_transform_files",
    "token_transform_occurrences", "grouped_math_script_occurrences", "induction_exercise_occurrences",
    "deferred_problem_tabs_replaced", "metadata_config_sha256",
)}))
