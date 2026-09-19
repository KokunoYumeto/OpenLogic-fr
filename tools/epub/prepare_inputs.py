"""Prepare the exact released sources in a fresh, task-owned build directory."""
from pathlib import Path
import json,hashlib,shutil,sys,re
E=Path(__file__).resolve().parent;ROOT=E.parents[1]
mode=sys.argv[1];assert mode in ("epub","pdf")
D=E/("conversion" if mode=="epub" else "direct-tex-check")
assert not D.exists(),"Use a fresh extracted package, or resume the existing build."
shutil.copytree(ROOT/"upstream",D/"source")
C=D/"source/locale/fr";shutil.copytree(ROOT/"fr",C)
contract=json.loads((E/"SOURCE_COVERAGE_CONTRACT.json").read_text(encoding="utf-8"))
for unit in contract["units"]:
 p=C/unit["path"];raw=p.read_bytes()
 assert hashlib.sha256(raw).hexdigest()==unit["sha256"]
 if mode=="epub":
  text=raw.decode("utf-8").replace("!!",r"\OLToken ").replace(r"0^\mathbb{R}",r"0^{\mathbb{R}}")
  def capital(m):
   article,token,plural=m.groups()
   return (r'\usetoken{A}{'+token+r'}~\usetoken{'+('p' if plural else 's')+'}{'+token+'}') if article else r'\usetoken{'+('P' if plural else 'S')+'}{'+token+'}'
  text=re.sub(r'\\OLToken \^(a?)\{([^}]+)\}(s?)',capital,text)
  p.write_bytes(text.encode("utf-8"))
if mode=="epub":
 for name in ["french-epub.cfg","reader.mk4"]:shutil.copyfile(E/name,C/name)
else:shutil.copyfile(ROOT/"fr/reader-cumulative.tex",C/"reader.tex")
print("Prepared",mode,"from",len(contract["units"]),"verified units.")
