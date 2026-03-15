# 🔥 Fire Detection System - Quick Start Guide

## ✅ Your Project is Now Working!

The fire detection system has been restored to a simple, working configuration.

## 🚀 How to Start the System:

### 1. Install Dependencies (if not already installed):
```bash
pip install -r requirements.txt
```

### 2. Start the Django Server:
```bash
python manage.py runserver
```

### 3. Open Your Browser:
Go to: **http://127.0.0.1:8000**

### 4. Allow Camera Permissions:
- Your browser will ask for camera permission
- Click "Allow" to enable camera access
- The fire detection will start automatically

## 📋 What's Working:

✅ **Django Server** - Running on simple SQLite database  
✅ **Camera Access** - Camera 0 detected and working (640x480, 15 FPS)  
✅ **YOLO AI Model** - Fire detection enabled (15.7GB RAM detected)  
✅ **Web Interface** - Professional dashboard with real-time feed  
✅ **SMS Alerts** - Twilio integration ready (configure in .env)  

## 🔧 Configuration:

### Basic Settings (already configured):
- **Database**: SQLite (simple, no setup needed)
- **Debug Mode**: Enabled for development
- **Camera**: Auto-detected and working
- **AI Model**: YOLO enabled with memory optimization

### Optional - SMS Alerts:
Edit the `.env` file to add your Twilio credentials:
```
TWILIO_ACCOUNT_SID=your_account_sid_here
TWILIO_AUTH_TOKEN=your_auth_token_here
TWILIO_PHONE_NUMBER=+1234567890
```

## 🎯 Features Available:

1. **Real-time Fire Detection** - AI-powered fire detection using YOLO
2. **Live Camera Feed** - See what the camera sees in real-time
3. **Instant Alerts** - Visual and audio alerts when fire is detected
4. **SMS Notifications** - Send SMS alerts (when Twilio is configured)
5. **Demo Mode** - Automatic fallback if camera issues occur
6. **Bilingual Support** - English and Hindi interface

## 🔍 Testing:

### Test Camera:
```bash
python test_camera.py
```

### Test Fire Detection:
1. Start the server: `python manage.py runserver`
2. Open browser: `http://127.0.0.1:8000`
3. Show a flame or fire image to the camera
4. System should detect and alert

## 🆘 If You Have Issues:

1. **Camera not working?** - Read `CAMERA_FIX_GUIDE.md`
2. **Server won't start?** - Make sure you're in the Fire_detector folder
3. **Dependencies missing?** - Run `pip install -r requirements.txt`
4. **Port already in use?** - Use `python manage.py runserver 8001`

## 📁 Project Structure:
```
Fire_detector/
├── manage.py              # Django management script
├── requirements.txt       # Simple dependencies only
├── .env                  # Configuration file
├── db.sqlite3            # Database (auto-created)
├── Fire_detector/        # Django project settings
├── Home/                 # Main application
├── ML_Model/             # AI model files
└── static/               # CSS, JS, images
```

## 🎉 You're All Set!

Your fire detection system is now working with a simple, clean configuration. No complex production settings, just pure functionality.

**Start Command**: `python manage.py runserver`  
**URL**: http://127.0.0.1:8000  
**Status**: ✅ Ready to detect fires!