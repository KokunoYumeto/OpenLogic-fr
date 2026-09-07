param(
  [Parameter(Mandatory=$true)][string]$ScratchRoot,
  [int]$MutexTimeoutMs = 1500
)
$ErrorActionPreference = 'Stop'
$repoRoot = (Resolve-Path -LiteralPath (Join-Path $PSScriptRoot '..')).Path
$scratchPath = [IO.Path]::GetFullPath($ScratchRoot)
if ($scratchPath -eq [IO.Path]::GetPathRoot($scratchPath)) { throw 'Refusing a drive-root build directory.' }
if (Test-Path -LiteralPath $scratchPath) { throw 'Use a fresh build directory; no existing files are overwritten.' }
New-Item -ItemType Directory -Path $scratchPath | Out-Null
Copy-Item -LiteralPath (Join-Path $repoRoot 'upstream') -Destination (Join-Path $scratchPath 'source') -Recurse
$sourceTree = Join-Path $scratchPath 'source'
$localized = Join-Path $sourceTree 'locale\fr'
Copy-Item -LiteralPath (Join-Path $repoRoot 'fr') -Destination $localized -Recurse
$receipt = [ordered]@{mutex='Global\InterlanguageTeXSlotV1'; timeout_ms=$MutexTimeoutMs; abandoned_recovery=$false; status='pending'; passes=@()}
$mutex = [Threading.Mutex]::new($false, 'Global\InterlanguageTeXSlotV1')
$acquired = $false
$texProcess = $null
$priorEpoch = $env:SOURCE_DATE_EPOCH
$priorForceDate = $env:FORCE_SOURCE_DATE
try {
  try { $acquired = $mutex.WaitOne($MutexTimeoutMs) }
  catch [Threading.AbandonedMutexException] { $acquired=$true; $receipt.abandoned_recovery=$true }
  if (-not $acquired) { $receipt.status='slot_occupied'; throw 'TeX slot occupied; continue translation and resume with a fresh build directory.' }
  $receipt.acquired_utc = [DateTime]::UtcNow.ToString('o')
  $env:SOURCE_DATE_EPOCH = '1788739200'
  $env:FORCE_SOURCE_DATE = '1'
  $receipt.source_date_epoch = $env:SOURCE_DATE_EPOCH
  $engine = (Get-Command xelatex.exe).Source
  $receipt.engine = $engine
  for ($passNumber=1; $passNumber -le 3; $passNumber++) {
    $stdoutPath = Join-Path $scratchPath "pass-$passNumber.stdout.txt"
    $stderrPath = Join-Path $scratchPath "pass-$passNumber.stderr.txt"
    $texProcess = Start-Process -FilePath $engine -ArgumentList @('-disable-installer','-interaction=nonstopmode','-halt-on-error','-file-line-error','-recorder','reader.tex') -WorkingDirectory $localized -RedirectStandardOutput $stdoutPath -RedirectStandardError $stderrPath -WindowStyle Hidden -PassThru
    $texProcess.WaitForExit()
    $texProcess.Refresh()
    $receipt.passes += @{pass=$passNumber; exit_code=$texProcess.ExitCode}
    if ($texProcess.ExitCode -ne 0) { throw "TeX failed on pass $passNumber; see captured output." }
    $texProcess = $null
  }
  $log = Get-Content -LiteralPath (Join-Path $localized 'reader.log') -Raw
  $receipt.log_findings = @([regex]::Matches($log,'(?m)^.*(?:Warning|Overfull|Undefined control|undefined references).*$') | ForEach-Object { $_.Value })
  $pdf = Join-Path $localized 'reader.pdf'
  $receipt.pdf_sha256 = (Get-FileHash -LiteralPath $pdf -Algorithm SHA256).Hash.ToLowerInvariant()
  $receipt.pdf_bytes = (Get-Item -LiteralPath $pdf).Length
  $receipt.status = 'built_requires_QA'
}
catch {
  if ($receipt.status -eq 'pending') { $receipt.status='failed' }
  $receipt.error = $_.Exception.Message
}
finally {
  if ($null -ne $texProcess -and -not $texProcess.HasExited) { $texProcess.WaitForExit() }
  if ($acquired) { $mutex.ReleaseMutex() }
  $env:SOURCE_DATE_EPOCH = $priorEpoch
  $env:FORCE_SOURCE_DATE = $priorForceDate
  $mutex.Dispose()
  $receipt.finished_utc = [DateTime]::UtcNow.ToString('o')
  $receipt | ConvertTo-Json -Depth 8 | Set-Content -LiteralPath (Join-Path $scratchPath 'BUILD_RECEIPT.json') -Encoding utf8
}
$receipt | ConvertTo-Json -Depth 8
if ($receipt.status -ne 'built_requires_QA') { exit 1 }
