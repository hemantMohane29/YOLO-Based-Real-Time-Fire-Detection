# 🔥 YOLO-Based Real-Time Fire Detection System

A professional-grade fire detection system powered by YOLOv8 AI model with real-time monitoring, SMS alerts, and web-based dashboard. Built with Django and optimized for cloud deployment.

![Fire Detection Demo](https://img.shields.io/badge/Status-Production%20Ready-brightgreen)
![Python](https://img.shields.io/badge/Python-3.8+-blue)
![Django](https://img.shields.io/badge/Django-5.2+-green)
![YOLOv8](https://img.shields.io/badge/YOLOv8-Ultralytics-orange)

## ✨ Features

### 🎯 Core Capabilities
- **Real-time Fire Detection** - YOLOv8-powered AI model with 90%+ accuracy
- **Live Camera Feed** - WebRTC-based video streaming with low latency
- **Smart Alerts** - Automatic SMS/WhatsApp notifications via Twilio
- **Professional Dashboard** - Modern web interface with real-time metrics
- **Multi-language Support** - English and Hindi alert messages

### 🛡️ Safety Features
- **Stability Buffer** - Prevents false alarms with confidence-based filtering
- **Emergency Contacts** - Automated alerts to multiple contacts
- **Manual Alert System** - One-click emergency notifications
- **System Monitoring** - Real-time performance and health metrics

### 🚀 Technical Features
- **Cloud-Ready** - Optimized for Render, Heroku, and other platforms
- **Memory Efficient** - Adaptive loading based on available resources
- **Demo Mode** - Fallback operation for resource-constrained environments
- **Responsive Design** - Works on desktop, tablet, and mobile devices

## 🏗️ Architecture

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   Web Browser   │◄──►│   Django Server  │◄──►│   YOLO Model    │
│                 │    │                  │    │                 │
│ • Live Video    │    │ • Fire Detection │    │ • AI Inference  │
│ • Dashboard     │    │ • SMS Alerts     │    │ • Confidence    │
│ • Controls      │    │ • API Endpoints  │    │ • Bounding Box  │
└─────────────────┘    └──────────────────┘    └─────────────────┘
                                │
                                ▼
                       ┌──────────────────┐
                       │   Twilio API     │
                       │                  │
                       │ • SMS Delivery   │
                       │ • WhatsApp       │
                       │ • Multi-contact  │
                       └──────────────────┘
```

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Webcam/Camera access
- Twilio account (optional, for SMS alerts)

### Local Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/hemantMohane29/YOLO-Based-Real-Time-Fire-Detection.git
   cd YOLO-Based-Real-Time-Fire-Detection/Fire_detector
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   # For full AI capabilities (requires 2GB+ RAM)
   pip install -r requirements-full.txt
   
   # For demo mode (lightweight)
   pip install -r requirements.txt
   ```

4. **Configure environment variables**
   ```bash
   cp .env.example .env
   # Edit .env with your Twilio credentials (optional)
   ```

5. **Run the application**
   ```bash
   cd Fire_detector
   python manage.py migrate
   python manage.py runserver
   ```

6. **Access the dashboard**
   Open http://localhost:8000 in your browser

## 🌐 Cloud Deployment

### Deploy to Render (Recommended)

[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com)

1. **Fork this repository** to your GitHub account

2. **Connect to Render**
   - Go to [render.com](https://render.com)
   - Click "New +" → "Web Service"
   - Connect your GitHub repository

3. **Configure deployment**
   ```yaml
   Name: fire-detector
   Environment: Python 3
   Build Command: ./build.sh
   Start Command: cd Fire_detector && gunicorn Fire_detector.wsgi:application
   ```

4. **Set environment variables**
   - `SECRET_KEY`: Auto-generate
   - `DEBUG`: `false`
   - `TWILIO_ACCOUNT_SID`: Your Twilio SID (optional)
   - `TWILIO_AUTH_TOKEN`: Your Twilio token (optional)

5. **Deploy**
   - Click "Create Web Service"
   - Your app will be live at `https://your-app-name.onrender.com`

### Other Platforms
- **Heroku**: Use `requirements-full.txt` and set `DISABLE_COLLECTSTATIC=1`
- **Railway**: Works out of the box with `render.yaml`
- **DigitalOcean**: Use Docker deployment with provided Dockerfile

## 📱 Usage

### Dashboard Overview
- **Live Feed**: Real-time camera stream with fire detection overlay
- **Detection Status**: Current fire detection confidence and status
- **System Metrics**: FPS, uptime, and performance indicators
- **Emergency Contacts**: Quick access to call emergency contacts
- **Manual Alerts**: Send immediate alerts to all contacts

### Fire Detection Process
1. **Camera Capture**: Continuous video stream processing
2. **AI Analysis**: YOLOv8 model analyzes each frame
3. **Confidence Scoring**: Assigns confidence percentage to detections
4. **Stability Check**: Filters false positives with buffer system
5. **Alert Trigger**: Sends SMS/WhatsApp when fire confirmed
6. **Dashboard Update**: Real-time UI updates with detection status

### SMS Alert System
- **Automatic Alerts**: Triggered when fire confidence > 50% for 6+ consecutive frames
- **Manual Alerts**: One-click emergency notifications
- **Multi-language**: English and Hindi message support
- **Cooldown Period**: 5-minute cooldown prevents spam
- **Multiple Contacts**: Alerts sent to all configured contacts

## ⚙️ Configuration

### Environment Variables

| Variable | Description | Required | Default |
|----------|-------------|----------|---------|
| `SECRET_KEY` | Django secret key | Yes | Auto-generated |
| `DEBUG` | Debug mode | No | `false` |
| `TWILIO_ACCOUNT_SID` | Twilio Account SID | No | - |
| `TWILIO_AUTH_TOKEN` | Twilio Auth Token | No | - |
| `TWILIO_WHATSAPP_FROM` | WhatsApp sender number | No | - |
| `TWILIO_PHONE_NUMBER` | SMS sender number | No | - |

### Model Configuration
```python
# Fire_detector/Home/views.py
CONF_THRESHOLD = 0.50  # Detection confidence threshold
ALERT_COOLDOWN = 300   # Seconds between alerts
STABILITY_BUFFER = 6   # Frames required for stable detection
```

### Contact Configuration
```python
# Fire_detector/Home/views.py
CONTACTS = [
    ("Name", "+1234567890"),
    # Add more contacts here
]
```

## 🧪 Testing

### Run Tests
```bash
python manage.py test
```

### Manual Testing
1. **Camera Test**: Verify video feed appears
2. **Detection Test**: Use fire images/videos to test detection
3. **Alert Test**: Use manual alert button to test SMS delivery
4. **Performance Test**: Monitor FPS and memory usage

### Demo Mode Testing
- Demo mode activates automatically on low-memory systems
- Simulates fire detection with random confidence scores
- All UI features remain functional
- Orange notification banner indicates demo mode

## 🔧 Troubleshooting

### Common Issues

**Camera not working**
```bash
# Check camera permissions in browser
# Ensure HTTPS for production (required for camera access)
```

**Memory issues on deployment**
```bash
# Use requirements.txt instead of requirements-full.txt
# App will run in demo mode automatically
```

**SMS not sending**
```bash
# Verify Twilio credentials in environment variables
# Check Twilio account balance and phone number verification
```

**Low FPS performance**
```bash
# Reduce image resolution in views.py
# Increase detection interval (currently 800ms)
```

### Performance Optimization

**For Production**
- Use `requirements-full.txt` with adequate RAM (2GB+)
- Enable GPU acceleration if available
- Optimize image resolution based on requirements
- Use CDN for static files

**For Development**
- Use `requirements.txt` for lightweight testing
- Demo mode provides full UI testing without ML overhead

## 📊 System Requirements

### Minimum Requirements (Demo Mode)
- **RAM**: 512MB
- **CPU**: 1 core
- **Storage**: 1GB
- **Network**: Broadband internet

### Recommended Requirements (Full AI)
- **RAM**: 2GB+
- **CPU**: 2+ cores
- **Storage**: 2GB
- **GPU**: Optional (CUDA-compatible for acceleration)

### Browser Support
- Chrome 80+ (recommended)
- Firefox 75+
- Safari 13+
- Edge 80+

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guidelines](CONTRIBUTING.md) for details.

### Development Setup
1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Make your changes and test thoroughly
4. Submit a pull request with detailed description

### Code Style
- Follow PEP 8 for Python code
- Use meaningful variable names
- Add comments for complex logic
- Include docstrings for functions

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Ultralytics** - YOLOv8 model and framework
- **OpenCV** - Computer vision processing
- **Twilio** - SMS and WhatsApp API services
- **Django** - Web framework
- **Render** - Cloud deployment platform

## 📞 Support

- **Issues**: [GitHub Issues](https://github.com/hemantMohane29/YOLO-Based-Real-Time-Fire-Detection/issues)
- **Discussions**: [GitHub Discussions](https://github.com/hemantMohane29/YOLO-Based-Real-Time-Fire-Detection/discussions)
- **Email**: [Your Email]

## 🔮 Roadmap

- [ ] Mobile app development
- [ ] Multi-camera support
- [ ] Cloud storage integration
- [ ] Advanced analytics dashboard
- [ ] Integration with fire department systems
- [ ] IoT sensor integration
- [ ] Machine learning model improvements

---

**⚠️ Important**: This system is designed to assist in fire detection but should not be the sole fire safety measure. Always maintain proper fire safety equipment and procedures.

**Made with by [Hemant Mohane](https://github.com/hemantMohane29)**
