"""Verify and copy the complete French edition into the build layout."""

from hashlib import sha256
import json
from pathlib import Path
import shutil


TOOLS = Path(__file__).resolve().parent
ROOT = TOOLS.parents[1]
BUILD = TOOLS / "direct-full"
MANIFEST = ROOT / "provenance/SOURCE_MANIFEST.jsonl"
GRAPH = ROOT / "provenance/FULL_READER_INPUTS.json"


def digest(path):
    return sha256(path.read_bytes()).hexdigest()


def main():
    graph = json.loads(GRAPH.read_text(encoding="utf-8"))
    assert digest(MANIFEST) == graph["manifest_sha256"]
    records = [json.loads(line) for line in MANIFEST.read_text(encoding="utf-8-sig").splitlines()]
    assert len(records) == 722
    expected = {row["path"]: row for row in graph["units"]}
    assert len(expected) == 722
    for row in records:
        relative = row["source_path"]
        declared = expected[relative]
        assert row["unit_id"] == declared["unit_id"]
        assert row["source_sha256"] == digest(ROOT / "upstream" / relative)
        assert declared["french_sha256"] == digest(ROOT / "fr" / relative)
    for path, expected_hash in graph["extra_french_source_sha256"].items():
        assert digest(ROOT / "fr" / path) == expected_hash, path
    reader = ROOT / "fr/reader-full.tex"
    assert digest(reader) == graph["reader_source_sha256"]
    BUILD.mkdir()
    upstream = BUILD / "source"
    locale = upstream / "locale/fr"
    shutil.copytree(ROOT / "upstream", upstream)
    shutil.copytree(ROOT / "fr", locale)
    shutil.copyfile(reader, locale / "reader.tex")
    scope = {
        "registered_source_units": 722,
        "potential_printable_units": 717,
        "source_only_compilation_drivers": 5,
        "reader_source_sha256": digest(reader),
        "manifest_sha256": digest(MANIFEST),
        "reader_graph": {
            "loaded_units": [{"path": row["path"]} for row in graph["units"] if row["loaded"]],
            "source_only_drivers": {
                row["unit_id"]: row["path"] for row in graph["units"] if not row["loaded"]
            },
            "non_manifest_local_tex_inputs": ["content/supplements/supplements.tex", "reader.tex"],
        },
    }
    assert len(scope["reader_graph"]["loaded_units"]) == 717
    (BUILD / "SOURCE_COVERAGE.json").write_text(
        json.dumps(scope, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n"
    )


if __name__ == "__main__":
    main()
