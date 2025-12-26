# 🔥 Fire Detection System - User Guide (Executable Version)

## 📋 Quick Start Guide

### 1. First Time Setup

**Download and Extract:**
1. Download `FireDetectionSystem_v1.0.zip`
2. Extract to a folder (e.g., `C:\FireDetection\`)
3. You should see these files:
   ```
   FireDetectionSystem.exe
   install_dependencies.bat
   README_EXECUTABLE.txt
   .env.example
   ```

**Install Dependencies:**
1. Right-click `install_dependencies.bat`
2. Select "Run as Administrator"
3. Wait for installation to complete (5-10 minutes)
4. Press any key when prompted

### 2. Running the Application

**Start the System:**
1. Double-click `FireDetectionSystem.exe`
2. Wait 30-60 seconds for startup
3. A browser window will open automatically
4. Allow camera access when prompted

**If Browser Doesn't Open:**
- Manually open your browser
- Go to: `http://localhost:8000`

## 🎯 Using the Fire Detection System

### Dashboard Overview

**Main Interface:**
- **Live Video Feed**: Shows your camera stream
- **Detection Status**: Current fire detection status
- **Confidence Meter**: AI confidence percentage
- **System Stats**: FPS, uptime, performance
- **Emergency Contacts**: Quick call buttons
- **Manual Alert**: Send immediate alerts

### Fire Detection Process

**Automatic Detection:**
1. System continuously monitors camera feed
2. AI analyzes each frame for fire/smoke
3. Requires 6 out of 10 frames to confirm fire
4. Automatically sends SMS alerts when confirmed
5. Plays alarm sound and updates dashboard

**Manual Alerts:**
1. Click "Send Alert" button for immediate notification
2. Bypasses automatic detection requirements
3. Sends SMS to all emergency contacts
4. Use for testing or emergency situations

## ⚙️ Configuration

### SMS Alert Setup (Optional)

**Get Twilio Account:**
1. Sign up at [twilio.com](https://twilio.com)
2. Get Account SID and Auth Token
3. Purchase a phone number for SMS

**Configure SMS:**
1. Copy `.env.example` to `.env`
2. Edit `.env` file with your credentials:
   ```
   TWILIO_ACCOUNT_SID=your_account_sid_here
   TWILIO_AUTH_TOKEN=your_auth_token_here
   TWILIO_PHONE_NUMBER=+1234567890
   ```
3. Restart the application

### Emergency Contacts

**Default Contacts:**
- Hemant Mohane: +91 79749 42457
- Zayed: +91 82523 55135
- Rudrashak: +91 91318 49771
- Abhishek: +91 93025 96728

**To Change Contacts:**
- Contact the developer for customization
- Or modify the source code if available

## 🔧 System Modes

### Full AI Mode
- **Requirements**: 4GB+ RAM
- **Features**: Real YOLO fire detection
- **Accuracy**: 90%+ detection accuracy
- **Status**: Shows "AI Detection Active"

### Demo Mode
- **Requirements**: 2GB RAM
- **Features**: Simulated fire detection
- **Purpose**: Testing and demonstration
- **Status**: Shows "Demo Mode" notification

## 🐛 Troubleshooting

### Application Won't Start

**Check Dependencies:**
```
1. Run install_dependencies.bat as Administrator
2. Ensure Python is installed (if prompted)
3. Check antivirus isn't blocking the executable
```

**Windows Defender Issues:**
```
1. Add executable to Windows Defender exclusions
2. Allow through Windows Firewall
3. Run as Administrator if needed
```

### Camera Not Working

**Browser Permissions:**
```
1. Click camera icon in browser address bar
2. Select "Always allow" for camera access
3. Refresh the page
```

**Camera In Use:**
```
1. Close other applications using camera
2. Restart the Fire Detection System
3. Try different browser if issues persist
```

### SMS Alerts Not Working

**Check Configuration:**
```
1. Verify .env file exists and has correct credentials
2. Check Twilio account balance
3. Ensure phone numbers are verified in Twilio
```

**Test SMS:**
```
1. Use "Send Alert" button to test
2. Check Twilio logs for delivery status
3. Verify recipient phone numbers are correct
```

### Performance Issues

**Low FPS:**
```
1. Close other applications
2. Use lower camera resolution
3. Ensure adequate lighting
```

**High Memory Usage:**
```
1. Restart the application periodically
2. Close unnecessary browser tabs
3. Check system has adequate RAM
```

## 📊 System Requirements

### Minimum Requirements
- **OS**: Windows 10/11 (64-bit)
- **RAM**: 2GB (Demo mode)
- **Storage**: 1GB free space
- **Camera**: Any USB/built-in webcam
- **Browser**: Chrome, Firefox, Edge

### Recommended Requirements
- **OS**: Windows 11 (64-bit)
- **RAM**: 8GB (Full AI mode)
- **Storage**: 2GB free space
- **Camera**: HD webcam (1080p)
- **Browser**: Chrome (latest version)

## 🔒 Security & Privacy

### Data Privacy
- **Local Processing**: All AI processing happens locally
- **No Cloud Upload**: Video never leaves your computer
- **SMS Only**: Only alert messages sent via Twilio
- **No Recording**: System doesn't save video files

### Network Security
- **Local Server**: Runs only on localhost (127.0.0.1)
- **No External Access**: Not accessible from internet
- **Firewall Safe**: Uses standard HTTP port locally

## 📞 Support & Help

### Getting Help
- **GitHub Issues**: Report bugs and request features
- **Email Support**: Contact developer directly
- **Documentation**: Check README files
- **Community**: Join discussions on GitHub

### Common Questions

**Q: Can I run this on multiple cameras?**
A: Current version supports one camera. Multi-camera support planned for future versions.

**Q: Does this work offline?**
A: Yes, fire detection works offline. SMS alerts require internet connection.

**Q: How accurate is the detection?**
A: 90%+ accuracy in good lighting conditions with the full AI model.

**Q: Can I customize the detection sensitivity?**
A: Currently requires code modification. GUI settings planned for future versions.

## 🔄 Updates & Maintenance

### Checking for Updates
- Visit GitHub repository for latest releases
- Download new version and replace executable
- Keep your `.env` configuration file

### Maintenance
- Restart application weekly for optimal performance
- Clear browser cache if interface issues occur
- Check Twilio account balance monthly

### Backup Configuration
- Keep a copy of your `.env` file
- Note any customizations made
- Save emergency contact information

## 📈 Advanced Usage

### Integration Options
- **Home Automation**: Trigger smart home devices
- **Security Systems**: Connect to existing alarms
- **Monitoring Services**: Log detection events
- **Custom Alerts**: Modify notification methods

### Performance Tuning
- **Camera Settings**: Adjust resolution and FPS
- **Detection Threshold**: Modify confidence levels
- **Alert Timing**: Customize cooldown periods
- **Resource Usage**: Optimize for your hardware

---

**🚨 Important Safety Notice**: This system is designed to assist in fire detection but should not be the sole fire safety measure. Always maintain proper fire safety equipment and procedures.

**📧 Support**: For technical support, feature requests, or bug reports, please contact the development team or visit the GitHub repository.

**🔥 Stay Safe**: Regular testing and maintenance ensure optimal performance of your fire detection system.