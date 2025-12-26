#!/usr/bin/env python3
"""
Fire Detection System Runner - Executable Version
Handles Django setup and server startup for standalone executable
"""

import os
import sys
import subprocess
import time
import webbrowser
import threading
from pathlib import Path

def get_base_path():
    """Get the base path for the application"""
    if getattr(sys, 'frozen', False):
        # Running as executable
        return Path(sys.executable).parent
    else:
        # Running as script
        return Path(__file__).parent.absolute()

def main():
    """Main entry point"""
    print("🔥 Fire Detection System Starting...")
    print("=" * 50)
    
    # Set up paths
    base_dir = get_base_path()
    django_dir = base_dir / "Fire_detector"
    
    print(f"📁 Base directory: {base_dir}")
    print(f"📁 Django directory: {django_dir}")
    
    # Check if Django directory exists
    if not django_dir.exists():
        print("❌ Django project directory not found!")
        print("📁 Looking for Fire_detector folder...")
        print("🔍 Please ensure all files are extracted properly")
        input("Press Enter to exit...")
        return
    
    # Change to Django directory
    os.chdir(django_dir)
    
    # Set Django settings
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Fire_detector.settings')
    
    try:
        # Import Django and set it up
        import django
        from django.core.management import execute_from_command_line
        from django.conf import settings
        
        django.setup()
        
        print("🔧 Setting up database...")
        execute_from_command_line(['manage.py', 'migrate', '--verbosity=0'])
        
        print("📁 Collecting static files...")
        execute_from_command_line(['manage.py', 'collectstatic', '--noinput', '--verbosity=0'])
        
        print("✅ Setup complete!")
        print("🚀 Starting server at http://localhost:8000")
        print("🌐 Browser will open automatically in 3 seconds...")
        print("🛑 Press Ctrl+C to stop the server")
        
        # Start browser after delay
        def open_browser():
            time.sleep(3)
            try:
                webbrowser.open('http://localhost:8000')
                print("🌐 Browser opened!")
            except Exception as e:
                print(f"⚠️ Could not open browser: {e}")
                print("📖 Please manually open: http://localhost:8000")
        
        threading.Thread(target=open_browser, daemon=True).start()
        
        # Start Django server
        execute_from_command_line(['manage.py', 'runserver', '127.0.0.1:8000', '--verbosity=1'])
        
    except ImportError as e:
        print(f"❌ Missing Django or dependencies: {e}")
        print("📦 Please ensure all required packages are installed")
        input("Press Enter to exit...")
    except KeyboardInterrupt:
        print("\n🛑 Server stopped by user")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        print("📋 Please check the error message above")
        input("Press Enter to exit...")

if __name__ == "__main__":
    main()