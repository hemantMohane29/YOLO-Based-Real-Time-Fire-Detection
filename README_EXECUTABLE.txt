# Fire Detection System - Executable Version

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
