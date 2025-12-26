# Deploy Fire Detector to Render

## Prerequisites
1. Create a [Render account](https://render.com)
2. Push your code to a GitHub repository
3. Set up Twilio account for SMS/WhatsApp alerts (optional)

## Deployment Steps

### 1. Connect GitHub Repository
- Go to Render Dashboard
- Click "New +" → "Web Service"
- Connect your GitHub repository containing this project

### 2. Configure Service
- **Name**: fire-detector (or your preferred name)
- **Environment**: Python 3
- **Build Command**: `./build.sh`
- **Start Command**: `cd Fire_detector && gunicorn Fire_detector.wsgi:application`
- **Plan**: Free (or upgrade as needed)

### 3. Set Environment Variables
In Render dashboard, add these environment variables:

**Required:**
- `SECRET_KEY`: Auto-generate or use a secure random string
- `DEBUG`: Set to `false` for production

**Optional (for Twilio features):**
- `TWILIO_ACCOUNT_SID`: Your Twilio Account SID
- `TWILIO_AUTH_TOKEN`: Your Twilio Auth Token  
- `TWILIO_WHATSAPP_FROM`: Your Twilio WhatsApp number (format: whatsapp:+1234567890)
- `TWILIO_PHONE_NUMBER`: Your Twilio SMS number (format: +1234567890)

### 4. Deploy
- Click "Create Web Service"
- Render will automatically build and deploy your app
- Your app will be available at: `https://your-service-name.onrender.com`

## Alternative: One-Click Deploy
You can also use the `render.yaml` file for one-click deployment:
1. In Render dashboard, click "New +" → "Blueprint"
2. Connect your repository
3. Render will read the `render.yaml` configuration automatically

## Important Notes
- The free tier may have cold starts (app sleeps after inactivity)
- For production use, consider upgrading to a paid plan
- The ML model file (`fire_model.pt`) will be included in the deployment
- Static files are served using WhiteNoise middleware

## Troubleshooting
- Check Render logs if deployment fails
- Ensure all dependencies are in `requirements.txt`
- Verify environment variables are set correctly