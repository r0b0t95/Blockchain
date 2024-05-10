Write-Host "if you want to active the enviroment press the letter [a]"

$option = Read-Host

if ($option -eq "a"){
     powershell .\.venv\Scripts\Activate.ps1
     Write-Host "python .venv activated"
}