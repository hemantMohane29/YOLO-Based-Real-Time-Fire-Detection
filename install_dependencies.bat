@echo off
echo ================================================
echo Fire Detection System - Installation Script
echo ================================================
echo.
echo Installing Python dependencies...
echo.

pip install django==5.2.9
pip install opencv-python-headless
pip install numpy
pip install pillow
pip install python-dotenv
pip install psutil
pip install twilio
pip install ultralytics
pip install torch torchvision torchaudio

echo.
echo ================================================
echo Installation complete!
echo ================================================
echo.
echo You can now run FireDetectionSystem.exe
echo.
pause
