param([Parameter(Mandatory=$true)][string]$ScratchRoot)
$ErrorActionPreference='Stop'
$root=(Resolve-Path -LiteralPath (Join-Path $PSScriptRoot '..')).Path
$dest=[IO.Path]::GetFullPath($ScratchRoot)
if (Test-Path -LiteralPath $dest) { throw 'Use a new scratch directory.' }
if ($dest.StartsWith($root+[IO.Path]::DirectorySeparatorChar,[StringComparison]::OrdinalIgnoreCase)) { throw 'Use a scratch directory outside the source tree.' }
New-Item -ItemType Directory -Path $dest | Out-Null
foreach ($folder in @('upstream','fr','tools')) { Copy-Item -LiteralPath (Join-Path $root $folder) -Destination (Join-Path $dest $folder) -Recurse }
$kit=Join-Path $dest 'tools\epub'
& python (Join-Path $kit 'prepare_inputs.py') pdf
if ($LASTEXITCODE -ne 0) { throw 'Input preparation failed.' }
& python (Join-Path $kit 'guard_tex4ebook.py') pdf-build pdf-compare
if ($LASTEXITCODE -ne 0) { throw 'PDF build failed; inspect the receipt.' }
