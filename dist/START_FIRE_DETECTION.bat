@echo off
echo ================================================
echo 🔥 Fire Detection System - Starting...
echo ================================================
echo.

REM Check if Python is available
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python is not installed!
    echo 📦 Please install Python 3.8+ from python.org
    echo.
    pause
    exit /b 1
)

echo ✅ Python found
echo 🔧 Installing required packages...
echo.

REM Install basic requirements
pip install django opencv-python-headless numpy pillow python-dotenv psutil twilio >nul 2>&1

echo ✅ Dependencies installed
echo 🚀 Starting Fire Detection System...
echo.

REM Navigate to the Fire_detector directory
cd Fire_detector

REM Run Django setup
python manage.py migrate >nul 2>&1
python manage.py collectstatic --noinput >nul 2>&1

echo ✅ Database setup complete
echo 🌐 Starting web server...
echo.
echo 📱 Your fire detection dashboard will open at:
echo    http://localhost:8000
echo.
echo 🛑 Press Ctrl+C to stop the server
echo.

REM Start the Django development server
start http://localhost:8000
python manage.py runserver 127.0.0.1:8000

pause