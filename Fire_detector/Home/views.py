from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from pathlib import Path
import base64
import cv2
import numpy as np
import json
import os
import time
import logging

# ================= LOGGING =================
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# ================= OPTIONAL TWILIO =================
try:
    from twilio.rest import Client as TwilioClient
    from twilio.base.exceptions import TwilioRestException
except Exception:
    TwilioClient = None
    TwilioRestException = Exception

# ================= OPTIONAL YOLO =================
try:
    from ultralytics import YOLO
except Exception:
    YOLO = None

# ================= BASE DIR =================
BASE_DIR = Path(__file__).resolve().parent.parent

# ================= LOAD YOLO MODEL =================
MODEL_PATH = BASE_DIR / "ML_Model" / "fire_model.pt"

model = None
if YOLO is not None:
    try:
        model = YOLO(str(MODEL_PATH))
        logger.info("YOLO model loaded successfully from %s", MODEL_PATH)
    except Exception as e:
        logger.exception("Failed to load YOLO model: %s", e)
else:
    logger.warning("YOLO not installed. Detection disabled.")

# ================= STABILITY BUFFER =================
fire_buffer = []

# ================= CONTACT LIST =================
CONTACTS = [
    ("Hemant Mohane", "+917974942457"),
    ("zayed", "+918252355135"),
    ("Rudrashak", "+919131849771"),
    ("abhishek", "+919302596728"),
]

ALERT_COOLDOWN = 300  # seconds
_last_alert_ts = 0

# ================= SEND SMS FUNCTION =================
def send_sms_to_contacts(message: str) -> bool:
    if TwilioClient is None:
        logger.warning("Twilio not installed. SMS skipped.")
        return False

    sid = os.environ.get("TWILIO_ACCOUNT_SID")
    token = os.environ.get("TWILIO_AUTH_TOKEN")
    wa_from = os.environ.get("TWILIO_WHATSAPP_FROM")
    sms_from = os.environ.get("TWILIO_PHONE_NUMBER")

    if not sid or not token:
        logger.error("Twilio SID/Auth token missing.")
        return False

    try:
        client = TwilioClient(sid, token)
    except Exception as e:
        logger.exception("Twilio client error: %s", e)
        return False

    sent_any = False
    body = f"🔥 FIRE ALERT 🔥\n{message}"

    for name, to in CONTACTS:
        # WhatsApp
        if wa_from:
            try:
                client.messages.create(
                    body=body,
                    from_=wa_from,
                    to=f"whatsapp:{to}"
                )
                sent_any = True
            except Exception as e:
                logger.error("WhatsApp failed to %s: %s", to, e)

        # SMS
        if sms_from:
            try:
                client.messages.create(
                    body=body,
                    from_=sms_from,
                    to=to
                )
                sent_any = True
            except Exception as e:
                logger.error("SMS failed to %s: %s", to, e)

    return sent_any

# ================= HOME VIEW =================
def home(request):
    return render(request, "Home/home.html")

# ================= DETECT VIEW =================
@csrf_exempt
def detect(request):
    global fire_buffer, _last_alert_ts

    if request.method != "POST":
        return JsonResponse({"error": "POST method required"}, status=405)

    if model is None:
        return JsonResponse({"error": "YOLO model not loaded"}, status=500)

    try:
        body = json.loads(request.body.decode("utf-8"))
        frame_data = body.get("frame")

        if not frame_data:
            return JsonResponse({"error": "No frame received"}, status=400)

        # -------- Base64 Decode --------
        if "," in frame_data:
            frame_data = frame_data.split(",")[1]

        img_bytes = base64.b64decode(frame_data)
        np_arr = np.frombuffer(img_bytes, np.uint8)
        frame = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)

        if frame is None:
            return JsonResponse({"error": "Invalid image"}, status=400)

        # -------- YOLO Prediction --------
        results = model.predict(frame, conf=0.35, imgsz=640)

        fire_detected = 0
        best_conf = 0.0
        CONF_THRESHOLD = 0.50

        if results and results[0].boxes:
            for box in results[0].boxes:
                cls_id = int(box.cls[0])
                conf = float(box.conf[0])
                if cls_id == 0 and conf >= CONF_THRESHOLD:
                    fire_detected = 1
                    best_conf = max(best_conf, conf)

        # -------- Stability Filter --------
        fire_buffer.append(fire_detected)
        if len(fire_buffer) > 10:
            fire_buffer.pop(0)

        stable_fire = 1 if sum(fire_buffer) >= 6 else 0

        # -------- SMS Throttling --------
        sms_sent = False
        now = time.time()
        if stable_fire == 1 and (now - _last_alert_ts) > ALERT_COOLDOWN:
            confidence_pct = round(best_conf * 100, 2)
            message = (
                f"Automatic fire detection.\n"
                f"Confidence: {confidence_pct}%\n"
                "Please check immediately.\n"
                "⚠️ आग का अलर्ट – कृपया तुरंत जांच करें।"
            )
            sms_sent = send_sms_to_contacts(message)
            if sms_sent:
                _last_alert_ts = now

        return JsonResponse({
            "fire": stable_fire,
            "conf": round(best_conf * 100, 2),
            "sms_sent": sms_sent
        })

    except Exception as e:
        logger.exception("Detect error: %s", e)
        return JsonResponse({"error": str(e)}, status=500)

# ================= MANUAL ALERT =================
@csrf_exempt
def send_alert(request):
    global _last_alert_ts

    if request.method != "POST":
        return JsonResponse({"error": "POST method required"}, status=405)

    try:
        body = json.loads(request.body.decode("utf-8"))
        raw_message = body.get("message", "Manual fire alert triggered")

        message = (
            f"{raw_message}\n"
            "This is a manual alert.\n"
            "⚠️ मैन्युअल आग अलर्ट – तुरंत जांच करें।"
        )

        sms_sent = send_sms_to_contacts(message)
        if sms_sent:
            _last_alert_ts = time.time()

        return JsonResponse({"sms_sent": sms_sent})

    except Exception as e:
        logger.exception("Manual alert error: %s", e)
        return JsonResponse({"error": str(e)}, status=500)
