"""
Simple build script for Fire Detection System executable
Creates a lightweight version without complex data bundling
"""

import os
import sys

def build_simple_exe():
    """Build a simple executable using PyInstaller"""
    print("🔥 Building Simple Fire Detection System Executable")
    print("=" * 60)
    
    # Simple PyInstaller command
    cmd = [
        "pyinstaller",
        "--onefile",
        "--console",
        "--name=FireDetectionSystem",
        "--add-data=Fire_detector;Fire_detector",
        "--hidden-import=django",
        "--hidden-import=django.core.management",
        "--hidden-import=django.core.management.commands.runserver",
        "--hidden-import=django.core.management.commands.migrate",
        "--hidden-import=django.core.management.commands.collectstatic",
        "--hidden-import=cv2",
        "--hidden-import=numpy",
        "--hidden-import=PIL",
        "--hidden-import=psutil",
        "--hidden-import=twilio",
        "--hidden-import=dotenv",
        "main.py"
    ]
    
    print("🔨 Running PyInstaller...")
    print("⏳ This will take 5-10 minutes...")
    
    # Join command and run
    cmd_str = " ".join(cmd)
    result = os.system(cmd_str)
    
    if result == 0:
        print("\n" + "=" * 60)
        print("🎉 BUILD SUCCESSFUL!")
        print("=" * 60)
        print("📦 Executable: dist/FireDetectionSystem.exe")
        print("📁 Size: ~50-100MB (lightweight version)")
        print("🚀 Ready to distribute!")
        
        # Create user instructions
        create_simple_instructions()
        
        return True
    else:
        print("❌ Build failed!")
        return False

def create_simple_instructions():
    """Create simple user instructions"""
    instructions = """# Fire Detection System - Quick Start

## How to Use:

1. **First Time Setup:**
   - Extract all files to a folder
   - Run FireDetectionSystem.exe
   - Wait 30-60 seconds for startup

2. **Using the System:**
   - Browser will open automatically
   - Allow camera access when prompted
   - System will start monitoring for fire

3. **Features:**
   - Real-time fire detection
   - Web dashboard interface
   - Manual alert system
   - Demo mode on low-memory systems

## System Requirements:
- Windows 10/11 (64-bit)
- 2GB RAM minimum
- Webcam or camera
- Internet browser

## Troubleshooting:
- If browser doesn't open: Go to http://localhost:8000
- If camera doesn't work: Check browser permissions
- If app won't start: Run as Administrator

## Support:
GitHub: https://github.com/hemantMohane29/YOLO-Based-Real-Time-Fire-Detection

Version: 1.0 (Lightweight)
"""
    
    with open('QUICK_START.txt', 'w') as f:
        f.write(instructions)
    
    print("✅ Quick start guide created: QUICK_START.txt")

if __name__ == "__main__":
    build_simple_exe()