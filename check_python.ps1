# PowerShell script to check for Python installation and provide guidance

Write-Host "============================================================" -ForegroundColor Cyan
Write-Host "Python Installation Checker" -ForegroundColor Cyan
Write-Host "============================================================" -ForegroundColor Cyan
Write-Host ""

# Check common Python installation locations
$pythonPaths = @(
    "C:\Python*",
    "C:\Program Files\Python*",
    "C:\Program Files (x86)\Python*",
    "$env:LOCALAPPDATA\Programs\Python\Python*",
    "$env:APPDATA\Python\Python*"
)

Write-Host "Checking for Python installations..." -ForegroundColor Yellow
$foundPython = $false

foreach ($pathPattern in $pythonPaths) {
    $paths = Get-ChildItem -Path $pathPattern -ErrorAction SilentlyContinue -Directory
    foreach ($path in $paths) {
        $pythonExe = Join-Path $path.FullName "python.exe"
        if (Test-Path $pythonExe) {
            Write-Host "  [OK] Found Python at: $pythonExe" -ForegroundColor Green
            $version = & $pythonExe --version 2>&1
            Write-Host "    Version: $version" -ForegroundColor Green
            $foundPython = $true
        }
    }
}

# Check if python is in PATH
Write-Host "`nChecking PATH environment variable..." -ForegroundColor Yellow
$pythonInPath = Get-Command python -ErrorAction SilentlyContinue
if ($pythonInPath) {
    $pythonPath = $pythonInPath.Source
    Write-Host "  Python found in PATH: $pythonPath" -ForegroundColor Cyan
    
    # Try to get version
    try {
        $version = python --version 2>&1
        if ($version -match "Python \d+\.\d+") {
            Write-Host "  Version: $version" -ForegroundColor Green
            $foundPython = $true
        } else {
            Write-Host "  [WARNING] This appears to be a Windows Store stub" -ForegroundColor Yellow
            Write-Host "  The python.exe in WindowsApps is not a real Python installation" -ForegroundColor Yellow
        }
    } catch {
        Write-Host "  [WARNING] Cannot execute Python from this location" -ForegroundColor Yellow
    }
}

Write-Host ""

if (-not $foundPython) {
    Write-Host "============================================================" -ForegroundColor Red
    Write-Host "Python is NOT installed!" -ForegroundColor Red
    Write-Host "============================================================" -ForegroundColor Red
    Write-Host ""
    Write-Host "The 'python' command points to a Windows Store stub that" -ForegroundColor Yellow
    Write-Host "redirects to the Microsoft Store. You need to install Python." -ForegroundColor Yellow
    Write-Host ""
    Write-Host "Installation Options:" -ForegroundColor Cyan
    Write-Host ""
    Write-Host "Option 1: Download from python.org (Recommended)" -ForegroundColor White
    Write-Host "  1. Go to: https://www.python.org/downloads/" -ForegroundColor Gray
    Write-Host "  2. Download the latest Python 3.x" -ForegroundColor Gray
    Write-Host "  3. During installation, CHECK 'Add Python to PATH'" -ForegroundColor Gray
    Write-Host "  4. Click 'Install Now'" -ForegroundColor Gray
    Write-Host ""
    Write-Host "Option 2: Install from Microsoft Store" -ForegroundColor White
    Write-Host "  1. Open Microsoft Store" -ForegroundColor Gray
    Write-Host "  2. Search for 'Python 3.12' or 'Python 3.11'" -ForegroundColor Gray
    Write-Host "  3. Click 'Install'" -ForegroundColor Gray
    Write-Host ""
    Write-Host "After installation, CLOSE and REOPEN your terminal," -ForegroundColor Yellow
    Write-Host "then run: python cosine_similarity.py" -ForegroundColor Yellow
} else {
    Write-Host "============================================================" -ForegroundColor Green
    Write-Host "Python is available! You can run your script with:" -ForegroundColor Green
    Write-Host "============================================================" -ForegroundColor Green
    Write-Host ""
    Write-Host "  python cosine_similarity.py" -ForegroundColor Cyan
    Write-Host ""
}
