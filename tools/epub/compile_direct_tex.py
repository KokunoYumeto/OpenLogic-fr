"""Invoked only inside guard_tex4ebook.py's already assigned suspended worker."""
from pathlib import Path
import os,shutil,subprocess,json,hashlib
E=Path(__file__).resolve().parent
D=E/'direct-tex-check'
C=D/'source/locale/fr'
env=os.environ.copy()
# The PDF witness uses the accepted native source, without EPUB wrappers.
env.pop('TEXINPUTS',None);env.pop('LUAINPUTS',None)
commands=[
 ['xelatex.exe','-disable-installer','-recorder','-interaction=nonstopmode','-halt-on-error','reader.tex'],
 ['bibtex.exe','-disable-installer','reader'],
 ['xelatex.exe','-disable-installer','-recorder','-interaction=nonstopmode','-halt-on-error','reader.tex'],
 ['xelatex.exe','-disable-installer','-recorder','-interaction=nonstopmode','-halt-on-error','reader.tex']
]
commands.append(commands[-1].copy())
for i,cmd in enumerate(commands,1):
 cmd[0]=shutil.which(cmd[0]);assert cmd[0]
 with open(D/('pass-'+str(i)+'.log'),'wb') as f:
  r=subprocess.run(cmd,cwd=C,env=env,stdout=f,stderr=subprocess.STDOUT,check=False)
 if r.returncode:raise RuntimeError('Compiler failed: pass '+str(i))
 print('Completed pass',i,flush=True)
log=(C/'reader.log').read_text(encoding='utf-8',errors='replace')
findings=[l for l in log.splitlines() if any(x in l for x in ['Warning','Overfull','Undefined','undefined references'])]
pdf=C/'reader.pdf'
report={'bytes':pdf.stat().st_size,'sha256':hashlib.sha256(pdf.read_bytes()).hexdigest(),'log_findings':findings,'status':'COMPILED_REQUIRES_COMPARISON'}
(D/'PDF_BUILD.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
print(json.dumps(report))
