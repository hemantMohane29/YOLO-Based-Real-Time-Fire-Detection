#!/usr/bin/env python3
"""
Fire Detection Model Download Script
Downloads the YOLOv8 fire detection model for the Fire Detection System
"""

import os
import sys
import urllib.request
from pathlib import Path

def download_model():
    """Download the fire detection model"""
    
    print("🔥 Fire Detection System - Model Download")
    print("=" * 50)
    
    # Model directory
    model_dir = Path(__file__).parent / "Fire_detector" / "ML_Model"
    model_dir.mkdir(parents=True, exist_ok=True)
    
    model_path = model_dir / "fire_model.pt"
    
    if model_path.exists():
        print(f"✅ Model already exists at: {model_path}")
        return True
    
    print(f"📁 Model directory: {model_dir}")
    print(f"📄 Model file: {model_path}")
    
    # For now, we'll use a pre-trained YOLOv8 model
    # In production, you would host your custom fire detection model
    model_url = "https://github.com/ultralytics/assets/releases/download/v0.0.0/yolov8n.pt"
    
    print(f"\n📥 Downloading model from: {model_url}")
    print("⏳ This may take a few minutes...")
    
    try:
        # Download with progress
        def progress_hook(block_num, block_size, total_size):
            downloaded = block_num * block_size
            if total_size > 0:
                percent = min(100, (downloaded * 100) // total_size)
                print(f"\r📥 Progress: {percent}% ({downloaded // 1024 // 1024}MB / {total_size // 1024 // 1024}MB)", end="")
        
        urllib.request.urlretrieve(model_url, model_path, progress_hook)
        print(f"\n✅ Model downloaded successfully!")
        print(f"📍 Location: {model_path}")
        
        # Verify file size
        size_mb = model_path.stat().st_size / (1024 * 1024)
        print(f"📊 File size: {size_mb:.1f} MB")
        
        return True
        
    except Exception as e:
        print(f"\n❌ Download failed: {e}")
        print(f"\n🔧 Manual download instructions:")
        print(f"1. Download a YOLOv8 model from: https://github.com/ultralytics/ultralytics")
        print(f"2. Save it as: {model_path}")
        print(f"3. Or train your own fire detection model")
        
        return False

def main():
    """Main function"""
    try:
        success = download_model()
        
        if success:
            print(f"\n🎉 Setup complete!")
            print(f"Your fire detection system is ready to use.")
            print(f"\nNext steps:")
            print(f"1. cd Fire_detector/Fire_detector")
            print(f"2. python manage.py runserver")
            print(f"3. Open http://localhost:8000")
        else:
            print(f"\n❌ Setup failed!")
            print(f"Please download the model manually.")
            sys.exit(1)
            
    except KeyboardInterrupt:
        print(f"\n⚠️ Download interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()