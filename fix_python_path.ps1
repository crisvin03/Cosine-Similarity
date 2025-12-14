# Script to fix Python PATH issue by disabling Windows Store alias
# Run this as Administrator if needed

Write-Host "============================================================" -ForegroundColor Cyan
Write-Host "Fixing Python PATH Issue" -ForegroundColor Cyan
Write-Host "============================================================" -ForegroundColor Cyan
Write-Host ""

# Method 1: Try using py launcher
Write-Host "Method 1: Trying Python Launcher (py)..." -ForegroundColor Yellow
$pyLauncher = "C:\Users\ACER\AppData\Local\Programs\Python\Launcher\py.exe"
if (Test-Path $pyLauncher) {
    Write-Host "  [OK] Found Python Launcher" -ForegroundColor Green
    Write-Host "  You can use: py cosine_similarity.py" -ForegroundColor Cyan
    Write-Host ""
    
    # Test it
    Write-Host "  Testing..." -ForegroundColor Yellow
    $version = & $pyLauncher --version 2>&1
    if ($version -match "Python") {
        Write-Host "  [OK] Python Launcher works!" -ForegroundColor Green
        Write-Host ""
        Write-Host "============================================================" -ForegroundColor Green
        Write-Host "SOLUTION: Use 'py' instead of 'python'" -ForegroundColor Green
        Write-Host "============================================================" -ForegroundColor Green
        Write-Host ""
        Write-Host "Run your script with:" -ForegroundColor Cyan
        Write-Host "  py cosine_similarity.py" -ForegroundColor White
        Write-Host ""
        exit 0
    }
}

# Method 2: Create an alias in PowerShell profile
Write-Host "Method 2: Creating PowerShell alias..." -ForegroundColor Yellow
$pythonExe = "C:\Users\ACER\AppData\Local\Programs\Python\Python314\python.exe"

if (Test-Path $pythonExe) {
    # Create alias for current session
    Set-Alias -Name python -Value $pythonExe -Scope Global -Force -ErrorAction SilentlyContinue
    
    Write-Host "  [OK] Created alias for current session" -ForegroundColor Green
    Write-Host ""
    
    # Test it
    Write-Host "  Testing..." -ForegroundColor Yellow
    $version = python --version 2>&1
    if ($version -match "Python 3.14") {
        Write-Host "  [OK] Alias works!" -ForegroundColor Green
        Write-Host ""
        Write-Host "============================================================" -ForegroundColor Green
        Write-Host "SOLUTION: Alias created for this session" -ForegroundColor Green
        Write-Host "============================================================" -ForegroundColor Green
        Write-Host ""
        Write-Host "You can now use: python cosine_similarity.py" -ForegroundColor Cyan
        Write-Host ""
        Write-Host "Note: This alias only works in this PowerShell session." -ForegroundColor Yellow
        Write-Host "To make it permanent, add to your PowerShell profile." -ForegroundColor Yellow
        Write-Host ""
    }
}

# Method 3: Instructions to disable Windows Store alias
Write-Host "============================================================" -ForegroundColor Yellow
Write-Host "PERMANENT FIX: Disable Windows Store Python Alias" -ForegroundColor Yellow
Write-Host "============================================================" -ForegroundColor Yellow
Write-Host ""
Write-Host "To permanently fix this, disable the Windows Store alias:" -ForegroundColor White
Write-Host ""
Write-Host "1. Press Win + I to open Settings" -ForegroundColor Gray
Write-Host "2. Go to: Apps > Advanced app settings > App execution aliases" -ForegroundColor Gray
Write-Host "3. Turn OFF 'App Installer' for python.exe and python3.exe" -ForegroundColor Gray
Write-Host "4. Restart your terminal" -ForegroundColor Gray
Write-Host ""
Write-Host "OR use the full path:" -ForegroundColor White
Write-Host "  C:\Users\ACER\AppData\Local\Programs\Python\Python314\python.exe cosine_similarity.py" -ForegroundColor Gray
Write-Host ""

