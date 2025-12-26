@echo off
echo ================================================
echo Fire Detection System - Executable Builder
echo ================================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.8+ and try again
    pause
    exit /b 1
)

echo Python found. Checking dependencies...
echo.

REM Install PyInstaller if not present
pip show pyinstaller >nul 2>&1
if errorlevel 1 (
    echo Installing PyInstaller...
    pip install pyinstaller
)

REM Install other build dependencies
echo Installing build dependencies...
pip install -r requirements_exe.txt

echo.
echo Starting build process...
echo This may take 10-15 minutes depending on your system...
echo.

REM Run the build script
python build_exe.py

if errorlevel 1 (
    echo.
    echo BUILD FAILED!
    echo Check the error messages above
    pause
    exit /b 1
)

echo.
echo ================================================
echo BUILD COMPLETED SUCCESSFULLY!
echo ================================================
echo.
echo Your executable is ready in the 'dist' folder:
echo   - FireDetectionSystem.exe
echo   - install_dependencies.bat
echo   - README_EXECUTABLE.txt
echo.
echo You can now distribute these files to users.
echo.
pause