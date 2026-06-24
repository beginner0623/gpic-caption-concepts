param(
    [Parameter(ValueFromRemainingArguments = $true)]
    [string[]] $PythonArgs
)

$ErrorActionPreference = "Stop"

$ProjectRoot = Split-Path -Parent (Split-Path -Parent $MyInvocation.MyCommand.Path)
$EnvPrefix = Join-Path $ProjectRoot ".mamba\env"
$PythonExe = Join-Path $EnvPrefix "python.exe"

if (-not (Test-Path $PythonExe)) {
    throw "Project Python was not found at $PythonExe. Create it with: micromamba create -y -p `"$EnvPrefix`" -f environment.yml"
}

& $PythonExe @PythonArgs
