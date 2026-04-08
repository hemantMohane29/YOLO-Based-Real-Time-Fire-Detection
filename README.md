# 🔥 YOLO-Based Real-Time Fire Detection System

A real-time fire detection web application powered by **YOLOv8** and **Django**, with automatic **SMS/WhatsApp alerts** via Twilio.

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)
![Django](https://img.shields.io/badge/Django-5.2-green?logo=django)
![YOLOv8](https://img.shields.io/badge/YOLOv8-Ultralytics-orange)
![OpenCV](https://img.shields.io/badge/OpenCV-4.8+-red?logo=opencv)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

## 📸 Demo

> Live camera feed → AI detects fire → Sends SMS/WhatsApp alert automatically

---

## ✨ Features

- 🎯 Real-time fire detection using YOLOv8 custom trained model
- 📹 Live webcam feed via browser (WebRTC)
- 🚨 Automatic SMS & WhatsApp alerts via Twilio
- 📊 Professional dashboard with confidence metrics
- 🔇 Audio alarm on fire detection
- 🌐 Works in browser — no app install needed
- ⚡ Demo mode when AI libraries are unavailable
- 🐳 Docker ready for cloud deployment

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | Django 5.2 |
| AI Model | YOLOv8 (Ultralytics) |
| Computer Vision | OpenCV |
| Alerts | Twilio SMS / WhatsApp |
| Frontend | HTML, CSS, JavaScript (WebRTC) |
| Deployment | Docker, Railway, Gunicorn |

---

## 🚀 Quick Start (Local)

### 1. Clone the repository

```bash
git clone https://github.com/hemantMohane29/YOLO-Based-Real-Time-Fire-Detection.git
cd YOLO-Based-Real-Time-Fire-Detection
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure environment

Edit `Fire_detector/.env`:

```env
DEBUG=True
SECRET_KEY=django-insecure-dev-key-only-for-development
ALLOWED_HOSTS=localhost,127.0.0.1

# Optional - for SMS alerts
TWILIO_ACCOUNT_SID=your_account_sid
TWILIO_AUTH_TOKEN=your_auth_token
TWILIO_PHONE_NUMBER=+1234567890
TWILIO_WHATSAPP_FROM=whatsapp:+14155238886
```

### 4. Run the server

```bash
cd Fire_detector/Fire_detector
python manage.py migrate
python manage.py runserver
```

### 5. Open in browser

```
http://127.0.0.1:8000
```

---

## 📁 Project Structure

```
YOLO-Based-Real-Time-Fire-Detection/
├── Dockerfile                        # Docker config for deployment
├── requirements.txt                  # Python dependencies
├── Fire_detector/
│   ├── .env                          # Environment variables
│   ├── Fire_detector/                # Django project
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   ├── Home/                         # Main app
│   │   ├── views.py                  # Fire detection logic
│   │   ├── urls.py
│   │   └── templates/Home/home.html  # Frontend UI
│   ├── ML_Model/
│   │   └── fire_model.pt             # YOLOv8 trained model
│   └── static/
│       ├── alarm.mp3                 # Alert sound
│       └── fire_bg.jpg               # Background image
```

---

## 🐳 Deploy with Docker

```bash
# Build image
docker build -t fire-detector .

# Run container
docker run -p 8000:8000 fire-detector
```

---

## 🚂 Deploy to Railway

1. Push code to GitHub
2. Go to [railway.app](https://railway.app)
3. Click **New Project → Deploy from GitHub**
4. Select this repository
5. Add environment variables:

```
DJANGO_SETTINGS_MODULE=Fire_detector.settings
DEBUG=False
SECRET_KEY=your-secret-key
ALLOWED_HOSTS=*.railway.app,*.up.railway.app
```

6. Click **Deploy** — Railway auto-detects the Dockerfile

---

## 📱 SMS / WhatsApp Alerts Setup

1. Create a [Twilio account](https://www.twilio.com)
2. Get your Account SID and Auth Token
3. Add to `.env` file:

```env
TWILIO_ACCOUNT_SID=ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
TWILIO_AUTH_TOKEN=your_auth_token
TWILIO_PHONE_NUMBER=+1234567890
TWILIO_WHATSAPP_FROM=whatsapp:+14155238886
```

Alerts are sent automatically when fire is detected with >50% confidence for 6+ consecutive frames.

---

## ⚙️ Configuration

| Variable | Default | Description |
|----------|---------|-------------|
| `DEBUG` | `True` | Django debug mode |
| `SECRET_KEY` | dev key | Django secret key |
| `ALLOWED_HOSTS` | `localhost,127.0.0.1` | Allowed hosts |
| `TWILIO_ACCOUNT_SID` | - | Twilio account SID |
| `TWILIO_AUTH_TOKEN` | - | Twilio auth token |
| `TWILIO_PHONE_NUMBER` | - | Twilio phone number |

---

## 🧠 How It Works

```
Browser Camera → Base64 Frame → Django /detect/ endpoint
       → OpenCV decode → YOLOv8 inference
       → Stability filter (6/10 frames)
       → Fire confirmed → Twilio SMS alert
       → JSON response → Frontend UI update
```

1. Browser captures webcam frames every second
2. Frames are sent as base64 to the `/detect/` API
3. YOLOv8 model runs inference on each frame
4. A stability buffer (6 out of 10 frames) prevents false alarms
5. On confirmed fire, Twilio sends SMS/WhatsApp to emergency contacts
6. Alert cooldown of 5 minutes prevents spam

---

## 🔧 Requirements

```
Django>=5.2.0
ultralytics>=8.0.0
torch>=2.0.0
torchvision>=0.15.0
opencv-python-headless>=4.8.0
numpy>=1.24.0
Pillow>=10.0.0
twilio>=8.0.0
gunicorn>=21.0.0
python-dotenv>=1.0.0
psutil>=5.9.0
```

---

## 🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first.

---

## 📄 License

This project is licensed under the [MIT License](Fire_detector/LICENSE).

---

## 👨‍💻 Author

**Hemant Mohane**
- GitHub: [@hemantMohane29](https://github.com/hemantMohane29) 🩷

---

> ⚠️ This system is designed to assist in fire detection but should not be the sole fire safety measure. Always maintain proper fire safety equipment and procedures....
