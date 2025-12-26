"""
Build script for creating Fire Detection System executable
Uses PyInstaller to create a standalone .exe file
"""

import os
import sys
import shutil
from pathlib import Path

def install_pyinstaller():
    """Install PyInstaller if not available"""
    try:
        import PyInstaller
        print("✅ PyInstaller already installed")
        return True
    except ImportError:
        print("📦 Installing PyInstaller...")
        os.system("pip install pyinstaller")
        try:
            import PyInstaller
            print("✅ PyInstaller installed successfully")
            return True
        except ImportError:
            print("❌ Failed to install PyInstaller")
            return False

def create_spec_file():
    """Create PyInstaller spec file"""
    spec_content = '''# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

# Data files to include
datas = [
    ('Fire_detector/Home/templates', 'Fire_detector/Home/templates'),
    ('Fire_detector/static', 'Fire_detector/static'),
    ('Fire_detector/ML_Model', 'Fire_detector/ML_Model'),
    ('Fire_detector/manage.py', 'Fire_detector'),
    ('Fire_detector/Fire_detector', 'Fire_detector/Fire_detector'),
    ('Fire_detector/Home', 'Fire_detector/Home'),
    ('.env', '.'),
]

# Hidden imports for Django and dependencies
hiddenimports = [
    'django',
    'django.core.management',
    'django.core.management.commands',
    'django.core.management.commands.runserver',
    'django.core.management.commands.migrate',
    'django.core.management.commands.collectstatic',
    'Fire_detector.settings',
    'Fire_detector.urls',
    'Fire_detector.wsgi',
    'Home.views',
    'Home.urls',
    'Home.apps',
    'Home.models',
    'cv2',
    'numpy',
    'PIL',
    'base64',
    'json',
    'time',
    'threading',
    'webbrowser',
    'pathlib',
    'logging',
    'psutil',
    'twilio',
    'twilio.rest',
    'dotenv',
    'ultralytics',
    'torch',
    'torchvision',
]

a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=datas,
    hiddenimports=hiddenimports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='FireDetectionSystem',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    cofile=None,
    icon='icon.ico' if os.path.exists('icon.ico') else None,
)
'''
    
    with open('FireDetectionSystem.spec', 'w') as f:
        f.write(spec_content)
    
    print("✅ Spec file created: FireDetectionSystem.spec")

def build_executable():
    """Build the executable using PyInstaller"""
    print("🔨 Building executable...")
    print("⏳ This may take several minutes...")
    
    # Run PyInstaller with the spec file
    cmd = "pyinstaller --clean FireDetectionSystem.spec"
    result = os.system(cmd)
    
    if result == 0:
        print("✅ Executable built successfully!")
        print("📁 Location: dist/FireDetectionSystem.exe")
        return True
    else:
        print("❌ Build failed!")
        return False

def create_installer_script():
    """Create a batch script for easy installation"""
    installer_content = '''@echo off
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
'''
    
    with open('install_dependencies.bat', 'w') as f:
        f.write(installer_content)
    
    print("✅ Installer script created: install_dependencies.bat")

def create_readme():
    """Create README for the executable"""
    readme_content = '''# Fire Detection System - Executable Version

## Quick Start

1. **First Time Setup:**
   - Run `install_dependencies.bat` as Administrator
   - Wait for all dependencies to install

2. **Run the Application:**
   - Double-click `FireDetectionSystem.exe`
   - Wait for the system to start (may take 30-60 seconds)
   - Browser will open automatically to http://localhost:8000

3. **Using the System:**
   - Allow camera access when prompted
   - The system will start monitoring for fire automatically
   - Configure SMS alerts by setting up Twilio credentials

## Configuration

### SMS Alerts (Optional)
Create a `.env` file with your Twilio credentials:
```
TWILIO_ACCOUNT_SID=your_account_sid
TWILIO_AUTH_TOKEN=your_auth_token
TWILIO_PHONE_NUMBER=+1234567890
```

## System Requirements

- Windows 10/11 (64-bit)
- 4GB RAM minimum (8GB recommended for AI features)
- Webcam or camera device
- Internet connection (for SMS alerts)

## Troubleshooting

### Application won't start
- Run `install_dependencies.bat` as Administrator
- Ensure antivirus isn't blocking the executable
- Check Windows Defender exclusions

### Camera not working
- Allow camera permissions in browser
- Check if other applications are using the camera
- Try refreshing the browser page

### SMS not working
- Verify Twilio credentials in `.env` file
- Check Twilio account balance
- Ensure phone numbers are verified

## Support

For issues and support:
- GitHub: https://github.com/hemantMohane29/YOLO-Based-Real-Time-Fire-Detection
- Email: [Your Email]

## Version Information

- Version: 1.0.0
- Build Date: 2025
- Python Version: 3.8+
- Django Version: 5.2.9
'''
    
    with open('README_EXECUTABLE.txt', 'w') as f:
        f.write(readme_content)
    
    print("✅ Executable README created: README_EXECUTABLE.txt")

def cleanup():
    """Clean up build files"""
    print("🧹 Cleaning up build files...")
    
    # Remove build directories
    if os.path.exists('build'):
        shutil.rmtree('build')
    if os.path.exists('__pycache__'):
        shutil.rmtree('__pycache__')
    
    # Remove spec file
    if os.path.exists('FireDetectionSystem.spec'):
        os.remove('FireDetectionSystem.spec')
    
    print("✅ Cleanup complete")

def main():
    """Main build process"""
    print("=" * 60)
    print("🔥 FIRE DETECTION SYSTEM - EXECUTABLE BUILDER")
    print("=" * 60)
    
    # Check if we're in the right directory
    if not os.path.exists('Fire_detector'):
        print("❌ Error: Fire_detector directory not found!")
        print("📁 Please run this script from the project root directory")
        return
    
    # Install PyInstaller
    if not install_pyinstaller():
        return
    
    # Create necessary files
    create_spec_file()
    create_installer_script()
    create_readme()
    
    # Build executable
    if build_executable():
        print("\n" + "=" * 60)
        print("🎉 BUILD SUCCESSFUL!")
        print("=" * 60)
        print("📦 Executable: dist/FireDetectionSystem.exe")
        print("🔧 Installer: install_dependencies.bat")
        print("📖 Instructions: README_EXECUTABLE.txt")
        print("=" * 60)
        print("\n📋 Distribution Package Contents:")
        print("   ├── FireDetectionSystem.exe")
        print("   ├── install_dependencies.bat")
        print("   └── README_EXECUTABLE.txt")
        print("\n🚀 Ready for distribution!")
    
    # Cleanup
    cleanup()

if __name__ == "__main__":
    main()