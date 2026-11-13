"""Repair specific XML serialization defects in raw TeX4ht reader output."""

from collections import Counter
from hashlib import sha256
from pathlib import Path
import json
import re
import sys


# Inside a MathML text run TeX4ht can emit a small-caps HTML span with
# a nonbreaking attribute separator. Neither the separator nor that
# span is valid here. Keep the label and its typography in a text run.
SPACE = rb"(?:\xc2\xa0|\xa0|&#(?:160|[xX]0*[aA]0);|&nbsp;)"
SMALL_CAPS = re.compile(
    rb"(<mtext\b[^>]*>)([^<]*)<span(?:" + SPACE + rb"|[ \t\r\n])+"
    rb"class=([\x22\x27])small-caps\3>([A-Za-z]+)</span>([^<]*)</mtext\s*>"
)
BAD_SMALL_CAPS = re.compile(rb"<span" + SPACE + rb"+class=[\x22\x27]small-caps")
LESS_THAN = re.compile(rb"(<mo\b[^>]*>\s*)<(\s*</mo\s*>)")

# TeX4ht serializes the dotted exponent base and its group terminators in
# the wrong order. The rest of the exponent remains an ordinary MathML tree.
DOTTED_EXPONENT = re.compile(
    rb'<mrow class="mathinner">(?:<mo\s+class="MathClass-punc" stretchy="false">'
    rb'\.</mo>){3}<msup><mrow\s*>\s*</mrow></mrow><mrow\s*>'
)

# The opening and closing brackets of this multiline formula occur in
# different table cells. The two bracket operators already have explicit sizes.
SPLIT_BRACKET_PAIR = re.compile(
    rb'<mrow>(<mo class="MathClass-open" fence="true" mathsize="1\.19em"\s*>\[</mo>)'
    rb'<mrow>(\s*</mtd></mtr><mtr><mtd\s+class="multline-star">(?:(?!</mtable>).)*?)'
    rb'</mrow>(<mo class="MathClass-close" fence="true" mathsize="1\.19em"\s*>\]</mo>)</mrow>',
    re.S,
)


def text_run_with_label(match):
    opening, before, _, label, after = match.groups()
    leading = opening + before + b"</mtext>" if before else b""
    trailing = opening + after + b"</mtext>" if after else b""
    return leading + b'<mtext class="small-caps">' + label + b"</mtext>" + trailing


def normalize(raw):
    repaired, small_caps = SMALL_CAPS.subn(text_run_with_label, raw)
    repaired, comparisons = LESS_THAN.subn(rb"\1&lt;\2", repaired)
    repaired, dotted_exponents = DOTTED_EXPONENT.subn(
        b'<msup><mrow><mo>&#x22F0;</mo></mrow><mrow>', repaired
    )
    repaired, split_brackets = SPLIT_BRACKET_PAIR.subn(rb"\1\2\3", repaired)
    spaces = repaired.count(b"&nbsp;")
    repaired = repaired.replace(b"&nbsp;", b"&#160;")
    return repaired, dict(
        small_caps_math_text_runs=small_caps,
        literal_less_than_math_operators=comparisons,
        dotted_exponent_bases=dotted_exponents,
        multiline_bracket_pairs=split_brackets,
        xml_safe_nonbreaking_spaces=spaces,
        unresolved_small_caps_separators=len(BAD_SMALL_CAPS.findall(repaired)),
    )


def main(root):
    totals = Counter()
    changed = []
    paths = sorted(root.glob("reader*.xhtml"))
    assert paths, root
    for path in paths:
        raw = path.read_bytes()
        repaired, counts = normalize(raw)
        totals.update(counts)
        if repaired != raw:
            path.write_bytes(repaired)
            changed.append(dict(
                document=path.name,
                input_sha256=sha256(raw).hexdigest(),
                output_sha256=sha256(repaired).hexdigest(),
                **counts,
            ))
    report = dict(documents=len(paths), totals=dict(totals), repairs=changed)
    (root / "PRE_DOM_XHTML.json").write_text(
        json.dumps(report, indent=2) + "\n", encoding="utf-8", newline="\n"
    )
    print(json.dumps(dict(documents=len(paths), totals=dict(totals))))


if __name__ == "__main__":
    main(Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else Path.cwd())
