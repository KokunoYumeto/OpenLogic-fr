"""One task-local Windows Job Object, created before resuming the worker.
The same thread owns the mutex through all descendants and immediate log checks.
"""
from pathlib import Path
import ctypes as c
from ctypes import wintypes as w
import _winapi,subprocess,os,sys,time,json,datetime,msvcrt,shutil
E=Path(__file__).resolve().parent
K=c.WinDLL("kernel32",use_last_error=True)
def api(name,args,result=w.BOOL):
 f=getattr(K,name);f.argtypes=args;f.restype=result;return f
CreateJob=api("CreateJobObjectW",[c.c_void_p,w.LPCWSTR],w.HANDLE)
SetJob=api("SetInformationJobObject",[w.HANDLE,c.c_int,c.c_void_p,w.DWORD])
QueryJob=api("QueryInformationJobObject",[w.HANDLE,c.c_int,c.c_void_p,w.DWORD,c.c_void_p])
Assign=api("AssignProcessToJobObject",[w.HANDLE,w.HANDLE])
TerminateJob=api("TerminateJobObject",[w.HANDLE,w.UINT])
Resume=api("ResumeThread",[w.HANDLE],w.DWORD)
Close=api("CloseHandle",[w.HANDLE])
CreateMutex=api("CreateMutexW",[c.c_void_p,w.BOOL,w.LPCWSTR],w.HANDLE)
Wait=api("WaitForSingleObject",[w.HANDLE,w.DWORD],w.DWORD)
Release=api("ReleaseMutex",[w.HANDLE])
Terminate=api("TerminateProcess",[w.HANDLE,w.UINT])
GetExit=api("GetExitCodeProcess",[w.HANDLE,c.POINTER(w.DWORD)])
class BasicLimit(c.Structure):
 _fields_=[("PerProcessUserTimeLimit",c.c_int64),("PerJobUserTimeLimit",c.c_int64),("LimitFlags",w.DWORD),("MinimumWorkingSetSize",c.c_size_t),("MaximumWorkingSetSize",c.c_size_t),("ActiveProcessLimit",w.DWORD),("Affinity",c.c_size_t),("PriorityClass",w.DWORD),("SchedulingClass",w.DWORD)]
class IO(c.Structure):
 _fields_=[(x,c.c_uint64) for x in ["ReadOperationCount","WriteOperationCount","OtherOperationCount","ReadTransferCount","WriteTransferCount","OtherTransferCount"]]
class Limits(c.Structure):
 _fields_=[("BasicLimitInformation",BasicLimit),("IoInfo",IO),("ProcessMemoryLimit",c.c_size_t),("JobMemoryLimit",c.c_size_t),("PeakProcessMemoryUsed",c.c_size_t),("PeakJobMemoryUsed",c.c_size_t)]
class Accounting(c.Structure):
 _fields_=[(x,c.c_int64) for x in ["TotalUserTime","TotalKernelTime","ThisPeriodTotalUserTime","ThisPeriodTotalKernelTime"]]+[(x,w.DWORD) for x in ["TotalPageFaultCount","TotalProcesses","ActiveProcesses","TotalTerminatedProcesses"]]
def check(ok):
 if not ok:raise c.WinError(c.get_last_error())
def counts(job):
 a=Accounting();check(QueryJob(job,1,c.byref(a),c.sizeof(a),None));return a
def now():return datetime.datetime.now(datetime.timezone.utc).isoformat()
def run(attempt,mode="convert",source_scope_units=83,worker_script=None):
 if not attempt.replace("-","").isalnum():raise ValueError("Invalid attempt name")
 capture=E/attempt;capture.mkdir(exist_ok=False)
 limit=180 if mode in ("convert","pdf-compare") else (25 if mode=="diagnostic" else (1 if mode=="test-timeout" else 10))
 r=dict(mutex="Global\\InterlanguageTeXSlotV1",timeout_ms=45000,whole_tree_timeout_seconds=limit,status="pending",acquired=False,abandoned_recovery=False,source_scope_units=source_scope_units,mode=mode,job_kill_on_close=True,created_suspended=True)
 mutex=job=ph=th=None;assigned=False;empty=True;streams=[]
 try:
  mutex=CreateMutex(None,False,r["mutex"]);check(mutex)
  outcome=Wait(mutex,45000)
  if outcome==258:r["status"]="slot_occupied";return r
  if outcome not in (0,128):raise c.WinError(c.get_last_error())
  r.update(acquired=True,abandoned_recovery=outcome==128,acquired_utc=now())
  job=CreateJob(None,None);check(job)
  limits=Limits();limits.BasicLimitInformation.LimitFlags=0x2000
  check(SetJob(job,9,c.byref(limits),c.sizeof(limits)))
  env=os.environ.copy()
  env.update(LUAINPUTS=E.as_posix()+"/dependencies/make4ht//;"+E.as_posix()+"/dependencies/tex4ebook//;",TEXINPUTS=E.as_posix()+"/dependencies/tex4ht-texlive/texmf-dist/tex/generic/tex4ht//;"+E.as_posix()+"/dependencies/tex4ebook//;",SOURCE_DATE_EPOCH="1788739200",FORCE_SOURCE_DATE="1")
  if mode in ("convert","diagnostic"):
   cmd=[shutil.which("texlua.exe"),str(E/"dependencies/tex4ebook/tex4ebook"),"-x","-f","epub3","-c","french-epub.cfg","reader.tex","mathml,daisy-","","","-disable-installer -recorder -interaction=nonstopmode -halt-on-error"]
  elif mode=="pdf-compare":
   cmd=[sys.executable,"-B","-X","utf8",str(worker_script or E/"compile_direct_tex.py")]
  else:
   # The parent exits immediately; its child stays alive and must remain owned.
   delay="20" if mode=="test-timeout" else "1.5"
   child="import time;time.sleep("+delay+")"
   parent="import subprocess,sys;subprocess.Popen([sys.executable,'-c',"+repr(child)+"])"
   cmd=[sys.executable,"-c",parent]
  if not cmd[0]:raise RuntimeError("texlua unavailable")
  streams=[open(capture/"stdout.txt","wb"),open(capture/"stderr.txt","wb"),open(os.devnull,"rb")]
  handles=[msvcrt.get_osfhandle(f.fileno()) for f in streams]
  for h in handles:os.set_handle_inheritable(h,True)
  si=subprocess.STARTUPINFO();si.dwFlags=subprocess.STARTF_USESTDHANDLES
  si.hStdOutput,si.hStdError,si.hStdInput=handles
  try:
   worker_cwd=E/"conversion/source/locale/fr" if mode in ("convert","diagnostic") else E
   ph,th,pid,tid=_winapi.CreateProcess(cmd[0],subprocess.list2cmdline(cmd),None,None,True,0x4|0x08000000,env,str(worker_cwd),si)
  finally:
   for h in handles:os.set_handle_inheritable(h,False)
  r["parent_pid"]=pid;empty=False
  check(Assign(job,ph));assigned=True
  if Resume(th)==0xffffffff:raise c.WinError(c.get_last_error())
  start=time.monotonic();r["started_utc"]=now();peak=0
  while True:
   a=counts(job);peak=max(peak,a.ActiveProcesses)
   if a.ActiveProcesses==0:empty=True;break
   code=w.DWORD();check(GetExit(ph,c.byref(code)))
   elapsed=time.monotonic()-start
   if elapsed>=limit or (code.value not in (0,259)):
    r["status"]="execution_timeout" if elapsed>=limit else "worker_failed"
    check(TerminateJob(job,124 if elapsed>=limit else code.value))
    r["owned_tree_terminated"]=True
    deadline=time.monotonic()+30
    while counts(job).ActiveProcesses and time.monotonic()<deadline:time.sleep(.1)
    empty=counts(job).ActiveProcesses==0
    if not empty:raise RuntimeError("Owned job termination not confirmed; fail closed")
    break
   time.sleep(.2)
  code=w.DWORD();check(GetExit(ph,c.byref(code)))
  r.update(exit_code=code.value,elapsed_seconds=round(time.monotonic()-start,3),peak_active_processes=peak,total_processes=counts(job).TotalProcesses,active_processes_at_end=counts(job).ActiveProcesses,job_empty_before_log_checks=empty)
  if r["status"]=="pending":r["status"]="converted_requires_QA" if mode=="convert" and code.value==0 else ("built_requires_QA" if mode=="pdf-compare" and code.value==0 else ("test_pass" if code.value==0 else "failed"))
 except BaseException as ex:
  r.update(status="guard_failure",error=str(ex))
 finally:
  if ph and not empty:
   if assigned:check(TerminateJob(job,125))
   else:check(Terminate(ph,125))
   deadline=time.monotonic()+30
   while time.monotonic()<deadline:
    empty=(counts(job).ActiveProcesses==0) if assigned else Wait(ph,0)==0
    if empty:break
    time.sleep(.1)
   r["cleanup_owned_tree_empty"]=empty
  for f in streams:f.close()
  for name in ["stdout","stderr"]:
   p=capture/(name+".txt")
   if p.exists():r[name+"_tail"]=p.read_text(encoding="utf-8",errors="replace").splitlines()[-20:]
  r["immediate_log_checks_utc"]=now()
  # Closing the job is also a kill-on-close backstop. No breakaway flags are set.
  if th:Close(th)
  if ph:Close(ph)
  if job:Close(job)
  if r["acquired"]:
   if not empty:
    r["status"]="fatal_unconfirmed_cleanup"
    (capture/"BUILD_RECEIPT.json").write_text(json.dumps(r,indent=2)+"\n")
    raise RuntimeError("Refusing explicit mutex release: owned-tree exit unconfirmed")
   check(Release(mutex));r["released_utc"]=now()
  if mutex:Close(mutex)
  r["finished_utc"]=now()
  (capture/"BUILD_RECEIPT.json").write_text(json.dumps(r,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 return r
if __name__=="__main__":
 result=run(sys.argv[1],sys.argv[2] if len(sys.argv)>2 else "convert")
 print(json.dumps(result,ensure_ascii=True))
 sys.exit(0 if result["status"] in ("converted_requires_QA","built_requires_QA","test_pass","slot_occupied") or (result["mode"]=="test-timeout" and result["status"]=="execution_timeout") else 1)
