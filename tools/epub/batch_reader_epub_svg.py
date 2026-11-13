"""Render TeX4ht's SVG picture requests in one dvisvgm invocation."""

from pathlib import Path
import re
import subprocess
import tempfile
from xml.etree import ElementTree


def picture_requests(log):
    requests = {}
    names = set()
    in_characters = False
    for line in log.splitlines():
        if line.startswith("--- characters ---"):
            in_characters = not line.removeprefix("--- characters ---").strip()
        if not line.startswith("--- needs ---") or in_characters:
            continue
        match = re.fullmatch(r"--- needs --- reader\.idv\[(\d+)\] ==> ([\w.-]+\.svg) ---", line)
        if not match:
            raise ValueError(f"Unsupported TeX4ht picture request: {line}")
        page, name = int(match[1]), match[2]
        if page in requests or name in names:
            raise ValueError(f"Repeated TeX4ht picture request: {line}")
        requests[page] = name
        names.add(name)
    if not requests:
        raise ValueError("TeX4ht recorded no SVG picture requests.")
    return requests


def main():
    requests = picture_requests(Path("reader.lg").read_text(encoding="utf-8", errors="replace"))
    print(f"Rendering {len(requests)} SVG images with dvisvgm", flush=True)

    with tempfile.TemporaryDirectory(prefix="ol-epub-svg-", dir=".") as staging:
        staged = Path(staging)
        pages = ",".join(str(page) for page in sorted(requests))
        with Path("reader-batch-svg.log").open("wb") as log:
            subprocess.run(
                ["dvisvgm", "-n", "--exact", "-c", "1.4,1.4", "-p", pages,
                 "-o", str(staged / "page-%p.svg"), "reader.idv"],
                stdout=log, stderr=subprocess.STDOUT, check=True,
            )
        generated = {
            int(path.stem.removeprefix("page-")): path for path in staged.glob("page-*.svg")
        }
        if set(generated) != set(requests):
            missing = sorted(set(requests) - set(generated))
            extra = sorted(set(generated) - set(requests))
            raise ValueError(f"DVI page mismatch. Missing {missing}. Unexpected {extra}.")
        for page, path in generated.items():
            if ElementTree.parse(path).getroot().tag != "{http://www.w3.org/2000/svg}svg":
                raise ValueError(f"DVI page {page} did not produce an SVG document.")
            if Path(requests[page]).exists():
                raise FileExistsError(requests[page])
        for page, path in generated.items():
            path.rename(requests[page])


if __name__ == "__main__":
    main()
