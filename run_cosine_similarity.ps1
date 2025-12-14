# PowerShell script to run cosine_similarity.py
# This script will try to find and use the correct Python executable

$scriptPath = Join-Path $PSScriptRoot "cosine_similarity.py"

if (-not (Test-Path $scriptPath)) {
    Write-Host "Error: cosine_similarity.py not found!" -ForegroundColor Red
    exit 1
}

# Try different Python commands (but skip Windows Store stub)
$pythonCommands = @("python", "python3", "py")

$pythonFound = $false
foreach ($cmd in $pythonCommands) {
    $python = Get-Command $cmd -ErrorAction SilentlyContinue
    if ($python) {
        # Skip Windows Store stub
        if ($python.Source -like "*WindowsApps*") {
            continue
        }
        try {
            # Test if it's a real Python installation
            $version = & $python.Source --version 2>&1
            if ($version -match "Python \d+\.\d+") {
                Write-Host "Using: $($python.Source)" -ForegroundColor Green
                Write-Host "Version: $version" -ForegroundColor Green
                Write-Host "Running cosine_similarity.py...`n" -ForegroundColor Cyan
                & $python.Source $scriptPath
                $pythonFound = $true
                break
            }
        } catch {
            Write-Host "Failed to run with $cmd" -ForegroundColor Yellow
        }
    }
}

if (-not $pythonFound) {
    # Try to find Python in common locations
    Write-Host "Python not found in PATH. Searching common locations..." -ForegroundColor Yellow
    
    $commonPaths = @(
        "$env:LOCALAPPDATA\Programs\Python\Python*\python.exe",
        "C:\Python*\python.exe",
        "C:\Program Files\Python*\python.exe",
        "C:\Program Files (x86)\Python*\python.exe"
    )
    
    foreach ($pathPattern in $commonPaths) {
        $pythonExe = Get-ChildItem -Path $pathPattern -ErrorAction SilentlyContinue | Select-Object -First 1
        if ($pythonExe) {
            Write-Host "Found Python at: $($pythonExe.FullName)" -ForegroundColor Green
            $version = & $pythonExe.FullName --version 2>&1
            Write-Host "Version: $version" -ForegroundColor Green
            Write-Host "Running cosine_similarity.py...`n" -ForegroundColor Cyan
            & $pythonExe.FullName $scriptPath
            $pythonFound = $true
            break
        }
    }
}

if (-not $pythonFound) {
    Write-Host ""
    Write-Host "============================================================" -ForegroundColor Red
    Write-Host "ERROR: Python not found!" -ForegroundColor Red
    Write-Host "============================================================" -ForegroundColor Red
    Write-Host ""
    Write-Host "Please install Python from:" -ForegroundColor Yellow
    Write-Host "  https://www.python.org/downloads/" -ForegroundColor White
    Write-Host ""
    Write-Host "Make sure to check 'Add Python to PATH' during installation." -ForegroundColor Yellow
    Write-Host ""
    Write-Host "Or run: .\check_python.ps1 to check your Python installation" -ForegroundColor Cyan
    exit 1
}
