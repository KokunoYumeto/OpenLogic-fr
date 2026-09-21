"""Invoked only inside the already assigned guarded worker."""
from __future__ import annotations

from pathlib import Path
import hashlib
import json
import os
import shutil
import subprocess


HERE = Path(__file__).resolve().parent
BUILD = HERE / "direct-tex-check"
SOURCE = BUILD / "source/locale/fr"
env = os.environ.copy()
env.pop("TEXINPUTS", None)
env.pop("LUAINPUTS", None)
commands = [
    ["xelatex.exe", "-disable-installer", "-recorder", "-interaction=nonstopmode", "-halt-on-error", "reader.tex"],
    ["bibtex.exe", "-disable-installer", "reader"],
    ["xelatex.exe", "-disable-installer", "-recorder", "-interaction=nonstopmode", "-halt-on-error", "reader.tex"],
    ["xelatex.exe", "-disable-installer", "-recorder", "-interaction=nonstopmode", "-halt-on-error", "reader.tex"],
]
commands.append(commands[-1].copy())
for index, command in enumerate(commands, 1):
    command[0] = shutil.which(command[0])
    assert command[0]
    with open(BUILD / ("pass-" + str(index) + ".log"), "wb") as stream:
        result = subprocess.run(command, cwd=SOURCE, env=env, stdout=stream, stderr=subprocess.STDOUT, check=False)
    if result.returncode:
        raise RuntimeError("Compiler failed: pass " + str(index))
    print("Completed pass", index, flush=True)
log = (SOURCE / "reader.log").read_text(encoding="utf-8", errors="replace")
findings = [
    line
    for line in log.splitlines()
    if any(marker in line for marker in ["Warning", "Overfull", "Undefined", "undefined references"])
]
pdf = SOURCE / "reader.pdf"
report = {
    "bytes": pdf.stat().st_size,
    "sha256": hashlib.sha256(pdf.read_bytes()).hexdigest(),
    "log_findings": findings,
    "status": "COMPILED_REQUIRES_COMPARISON",
}
(BUILD / "PDF_BUILD.json").write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
print(json.dumps(report))
