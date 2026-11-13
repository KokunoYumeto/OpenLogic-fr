"""Compile the frozen full reader inside the machine-wide TeX guard."""

from pathlib import Path
import hashlib
import json
import os
import re
import shutil
import subprocess
BUILD = Path(__file__).resolve().parent / "direct-full"
COMPILE = BUILD / "source/locale/fr"
coverage = json.loads((BUILD / "SOURCE_COVERAGE.json").read_text(encoding="utf-8"))
assert coverage["potential_printable_units"] == 717
reader = COMPILE / "reader.tex"
assert hashlib.sha256(reader.read_bytes()).hexdigest() == coverage["reader_source_sha256"]

xelatex, bibtex = shutil.which("xelatex.exe"), shutil.which("bibtex.exe")
assert xelatex and bibtex
env = os.environ.copy()
env.pop("TEXINPUTS", None)
env.pop("LUAINPUTS", None)
tex = [xelatex, "-disable-installer", "-recorder",
       "-interaction=nonstopmode", "-halt-on-error", "reader.tex"]


def citation_keys():
    aux = COMPILE / "reader.aux"
    if not aux.exists():
        return frozenset()
    value = aux.read_text(encoding="utf-8", errors="replace")
    return frozenset(key.strip() for group in re.findall(r"\\citation\{([^}]*)\}", value)
                     for key in group.split(",") if key.strip())


last_bib_keys = frozenset()
previous_aux = None
converged = False
bib_passes = []
for number in range(1, 7):
    keys_before = citation_keys()
    if number > 1 and keys_before and keys_before != last_bib_keys:
        with (COMPILE / f"bibtex-before-{number}.log").open("wb") as stream:
            result = subprocess.run([bibtex, "-disable-installer", "reader"],
                                    cwd=COMPILE, env=env, stdout=stream,
                                    stderr=subprocess.STDOUT)
        if result.returncode:
            raise RuntimeError(f"BibTeX failed before XeLaTeX pass {number}")
        last_bib_keys = keys_before
        bib_passes.append(number)
    with (COMPILE / f"pass-{number}.log").open("wb") as stream:
        result = subprocess.run(tex, cwd=COMPILE, env=env,
                                stdout=stream, stderr=subprocess.STDOUT)
    if result.returncode:
        raise RuntimeError(f"XeLaTeX pass {number} failed")
    print(f"Completed XeLaTeX pass {number}", flush=True)
    current_aux = (COMPILE / "reader.aux").read_bytes()
    keys_after = citation_keys()
    if number >= 3 and current_aux == previous_aux and keys_after == last_bib_keys:
        converged = True
        break
    previous_aux = current_aux
if not converged:
    raise RuntimeError("Auxiliary references and citations did not converge in six passes")

pdf = COMPILE / "reader.pdf"
log = (COMPILE / "reader.log").read_text(encoding="utf-8", errors="replace")
findings = [line for line in log.splitlines()
            if any(term in line for term in
                   ("Warning", "Overfull", "Undefined", "undefined references"))]
report = {
    "status": "COMPILED_REQUIRES_VISUAL_QA",
    "source_scope_units": 722,
    "potential_printable_units": 717,
    "source_only_compilation_drivers": 5,
    "pdf": pdf.name,
    "bytes": pdf.stat().st_size,
    "sha256": hashlib.sha256(pdf.read_bytes()).hexdigest(),
    "xelatex_passes": number,
    "bibtex_passes_before": bib_passes,
    "citation_keys_stable": True,
    "log_findings": findings,
}
(COMPILE / "PDF_BUILD.json").write_text(
    json.dumps(report, ensure_ascii=False, indent=2) + "\n",
    encoding="utf-8", newline="\n",
)
print(json.dumps({"status": report["status"], "pdf_sha256": report["sha256"],
                  "bytes": report["bytes"], "xelatex_passes": number,
                  "log_findings": len(findings)}), flush=True)
