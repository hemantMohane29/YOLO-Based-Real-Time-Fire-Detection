# Camera Access Fix Guide

If you're experiencing camera access issues, follow these steps:

## For Windows Users:

### 1. Check Camera Permissions
- Go to **Settings** > **Privacy & Security** > **Camera**
- Make sure "Camera access" is turned **ON**
- Make sure "Let apps access your camera" is turned **ON**
- Make sure "Let desktop apps access your camera" is turned **ON**

### 2. Check Browser Permissions
- In your browser (Chrome/Edge/Firefox), go to the fire detection website
- Look for a camera icon in the address bar
- Click it and select "Allow" for camera access
- If blocked, click the camera icon and change to "Allow"

### 3. Test Camera Access
Run the camera test script:
```bash
python test_camera.py
```

### 4. Common Issues and Solutions

**Issue: "Camera not found" or "Permission denied"**
- Solution: Restart your browser and allow camera permissions
- Make sure no other applications are using the camera

**Issue: Camera works in other apps but not in browser**
- Solution: Clear browser cache and cookies
- Try a different browser (Chrome recommended)

**Issue: Black screen in camera feed**
- Solution: Check if camera is being used by another application
- Restart the Django server: `python manage.py runserver`

### 5. Browser-Specific Fixes

**Chrome:**
- Go to `chrome://settings/content/camera`
- Make sure the site is not blocked
- Add your localhost to allowed sites

**Firefox:**
- Go to `about:preferences#privacy`
- Under Permissions, click "Settings" next to Camera
- Make sure localhost is allowed

**Edge:**
- Go to `edge://settings/content/camera`
- Make sure camera access is allowed for localhost

## Testing Steps:

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the server:**
   ```bash
   python manage.py runserver
   ```

3. **Open browser and go to:**
   ```
   http://127.0.0.1:8000
   ```

4. **Allow camera permissions when prompted**

5. **You should see the camera feed working**

## If Still Not Working:

1. Check if your camera works in other applications
2. Try using a different browser
3. Restart your computer
4. Make sure your camera drivers are up to date

## Demo Mode:
If camera still doesn't work, the system will automatically switch to demo mode with a sample fire detection image.