#!/usr/bin/env python3
"""
Fire Detection System - Standalone Executable Entry Point
This script starts the Django development server for the fire detection system.
"""

import os
import sys
import subprocess
import threading
import time
import webbrowser
from pathlib import Path

# Determine if running as executable
if getattr(sys, 'frozen', False):
    # Running as executable
    current_dir = Path(sys.executable).parent
    django_dir = current_dir / "Fire_detector"
    executable_mode = True
else:
    # Running as script
    current_dir = Path(__file__).parent.absolute()
    django_dir = current_dir / "Fire_detector"
    executable_mode = False

# Add paths to Python path
sys.path.insert(0, str(current_dir))
sys.path.insert(0, str(django_dir))

# Set Django settings module
if executable_mode:
    # Load executable-specific settings
    import exe_settings
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Fire_detector.settings')
else:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Fire_detector.settings')

def setup_django():
    """Initialize Django application"""
    try:
        import django
        from django.core.management import execute_from_command_line
        from django.conf import settings
        
        django.setup()
        
        # Change to Django directory
        os.chdir(django_dir)
        
        # Run migrations
        print("🔧 Setting up database...")
        execute_from_command_line(['manage.py', 'migrate', '--verbosity=0'])
        
        # Collect static files
        print("📁 Collecting static files...")
        execute_from_command_line(['manage.py', 'collectstatic', '--noinput', '--verbosity=0'])
        
        print("✅ Django setup complete!")
        return True
        
    except Exception as e:
        print(f"❌ Django setup failed: {e}")
        return False

def start_server():
    """Start Django development server"""
    try:
        import django
        from django.core.management import execute_from_command_line
        
        print("🚀 Starting Fire Detection System...")
        print("📡 Server will be available at: http://localhost:8000")
        print("🔥 Fire Detection Dashboard loading...")
        
        # Start Django server
        execute_from_command_line(['manage.py', 'runserver', '127.0.0.1:8000', '--verbosity=1'])
        
    except KeyboardInterrupt:
        print("\n🛑 Server stopped by user")
    except Exception as e:
        print(f"❌ Server error: {e}")
        input("Press Enter to exit...")

def open_browser():
    """Open browser after server starts"""
    time.sleep(3)  # Wait for server to start
    try:
        webbrowser.open('http://localhost:8000')
        print("🌐 Opening browser...")
    except Exception as e:
        print(f"⚠️ Could not open browser automatically: {e}")
        print("📖 Please manually open: http://localhost:8000")

def check_dependencies():
    """Check if required packages are available"""
    required_packages = [
        'django',
        'opencv-python',
        'numpy',
        'pillow'
    ]
    
    missing_packages = []
    for package in required_packages:
        try:
            __import__(package.replace('-', '_'))
        except ImportError:
            missing_packages.append(package)
    
    if missing_packages:
        print(f"❌ Missing packages: {', '.join(missing_packages)}")
        print("📦 Please install missing packages or use the full installer")
        return False
    
    return True

def main():
    """Main entry point"""
    print("=" * 60)
    print("🔥 FIRE DETECTION SYSTEM - STANDALONE VERSION")
    print("=" * 60)
    print("🤖 AI-Powered Real-time Fire Detection")
    print("📱 Web-based Dashboard with SMS Alerts")
    print("🛡️ Professional Safety Monitoring System")
    print("=" * 60)
    
    # Check dependencies
    if not check_dependencies():
        input("Press Enter to exit...")
        return
    
    # Setup Django
    if not setup_django():
        input("Press Enter to exit...")
        return
    
    # Start browser in separate thread
    browser_thread = threading.Thread(target=open_browser, daemon=True)
    browser_thread.start()
    
    # Start server (blocking)
    start_server()

if __name__ == "__main__":
    main()