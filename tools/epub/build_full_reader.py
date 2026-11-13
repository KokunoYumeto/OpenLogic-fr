"""Build the complete French PDF or EPUB under the shared Windows TeX guard."""

import argparse
import json
import os
from pathlib import Path
import subprocess
import sys

import guard_tex4ebook


TOOLS = Path(__file__).resolve().parent
PDF_DIR = TOOLS / "direct-full/source/locale/fr"


def run_python(script, *args):
    subprocess.run([sys.executable, "-B", "-X", "utf8", str(TOOLS / script), *map(str, args)], check=True)


def verify_reader_inputs(directory, source_scope):
    expected = {row["path"] for row in source_scope["reader_graph"]["loaded_units"]}
    excluded = set(source_scope["reader_graph"]["source_only_drivers"].values())
    locale = directory.resolve()
    loaded = set()
    for line in (locale / "reader.fls").read_text(encoding="utf-8").splitlines():
        if not line.startswith("INPUT ") or not line.endswith(".tex"):
            continue
        path = (locale / line[6:]).resolve()
        if path.is_relative_to(locale):
            loaded.add(path.relative_to(locale).as_posix())
    if expected - loaded or excluded & loaded:
        raise ValueError(f"Reader input mismatch: missing {sorted(expected - loaded)}, unexpected {sorted(excluded & loaded)}")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("format", choices=("pdf", "epub"))
    parser.add_argument("attempt", help="Name for a new guarded build attempt")
    args = parser.parse_args()
    contract = TOOLS / "direct-full/SOURCE_COVERAGE.json"
    if not contract.is_file():
        run_python("prepare_full_reader.py")
    source_scope = json.loads(contract.read_text(encoding="utf-8"))
    if args.format == "pdf":
        os.environ["INTERLANGUAGE_PDF_COMPARE_TIMEOUT"] = "900"
        receipt = guard_tex4ebook.run(
            args.attempt, "pdf-compare", source_scope_units=722,
            worker_script=TOOLS / "compile_full_reader.py", slot_timeout_ms=0, full_reader=True,
        )
        success = "built_requires_QA"
        if receipt["status"] == success:
            verify_reader_inputs(PDF_DIR, source_scope)
    else:
        if not (TOOLS / "FULL_EPUB_SOURCE_COVERAGE.json").is_file():
            run_python("prepare_full_epub.py")
        receipt = guard_tex4ebook.run(
            args.attempt, "convert", source_scope_units=722,
            slot_timeout_ms=0, full_reader=True,
        )
        success = "converted_requires_QA"
        if receipt["status"] == success:
            verify_reader_inputs(TOOLS / "conversion/source/locale/fr", source_scope)
            candidate = TOOLS / "openlogic-fr.epub"
            run_python("repair_epub_generated_navigation.py", TOOLS / "conversion/source/locale/fr/reader.epub", candidate)
            run_python("inspect_epub.py", candidate, 722)
    print(receipt["status"])
    if receipt["status"] == success:
        print(PDF_DIR / "reader.pdf" if args.format == "pdf" else TOOLS / "openlogic-fr.epub")
        return 0
    return 2 if receipt["status"] == "slot_occupied" else 1


if __name__ == "__main__":
    raise SystemExit(main())
