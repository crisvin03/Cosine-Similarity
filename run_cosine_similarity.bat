@echo off
REM Batch file to run cosine_similarity.py
REM This will try to find Python and run the script

echo ============================================================
echo Running Cosine Similarity Algorithm
echo ============================================================
echo.

REM Try python command
python --version >nul 2>&1
if %errorlevel% == 0 (
    echo Using Python from PATH...
    echo.
    python cosine_similarity.py
    goto :end
)

REM Try python3 command
python3 --version >nul 2>&1
if %errorlevel% == 0 (
    echo Using Python3 from PATH...
    echo.
    python3 cosine_similarity.py
    goto :end
)

REM Try py launcher
py --version >nul 2>&1
if %errorlevel% == 0 (
    echo Using Python Launcher (py)...
    echo.
    py cosine_similarity.py
    goto :end
)

REM Try to find Python in common installation location
if exist "%LOCALAPPDATA%\Programs\Python\Python*\python.exe" (
    for %%P in ("%LOCALAPPDATA%\Programs\Python\Python*\python.exe") do (
        echo Found Python at: %%P
        echo.
        %%P cosine_similarity.py
        goto :end
    )
)

REM If we get here, Python is not found
echo ============================================================
echo ERROR: Python not found!
echo ============================================================
echo.
echo Please install Python from:
echo   https://www.python.org/downloads/
echo.
echo Make sure to check "Add Python to PATH" during installation.
echo.
echo Or run: check_python.ps1 for more information
echo.
pause

:end

