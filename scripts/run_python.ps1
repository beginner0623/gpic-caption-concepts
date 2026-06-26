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

$Env:PATH = @(
    $EnvPrefix
    (Join-Path $EnvPrefix "Scripts")
    (Join-Path $EnvPrefix "Library\bin")
    (Join-Path $EnvPrefix "Library\usr\bin")
    (Join-Path $EnvPrefix "Library\mingw-w64\bin")
    $Env:PATH
) -join [IO.Path]::PathSeparator

& $PythonExe @PythonArgs
