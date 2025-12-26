"""
Django settings override for executable version
This file contains settings optimized for standalone executable
"""

import os
import sys
from pathlib import Path

# Determine if running as executable
if getattr(sys, 'frozen', False):
    # Running as executable
    BASE_DIR = Path(sys.executable).parent
    EXECUTABLE_MODE = True
else:
    # Running as script
    BASE_DIR = Path(__file__).resolve().parent / "Fire_detector"
    EXECUTABLE_MODE = False

# Override settings for executable
if EXECUTABLE_MODE:
    # Database path for executable
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'fire_detection.db',
        }
    }
    
    # Static files for executable
    STATIC_URL = '/static/'
    STATIC_ROOT = BASE_DIR / 'staticfiles'
    STATICFILES_DIRS = [
        BASE_DIR / 'Fire_detector' / 'static',
    ]
    
    # Templates for executable
    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [BASE_DIR / 'Fire_detector' / 'templates'],
            'APP_DIRS': True,
            'OPTIONS': {
                'context_processors': [
                    'django.template.context_processors.debug',
                    'django.template.context_processors.request',
                    'django.contrib.auth.context_processors.auth',
                    'django.contrib.messages.context_processors.messages',
                ],
            },
        },
    ]
    
    # Model path for executable
    MODEL_PATH = BASE_DIR / 'Fire_detector' / 'ML_Model' / 'fire_model.pt'
    
    # Logging for executable
    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'handlers': {
            'file': {
                'level': 'INFO',
                'class': 'logging.FileHandler',
                'filename': BASE_DIR / 'fire_detection.log',
            },
            'console': {
                'level': 'INFO',
                'class': 'logging.StreamHandler',
            },
        },
        'loggers': {
            'django': {
                'handlers': ['file', 'console'],
                'level': 'INFO',
                'propagate': True,
            },
            'Home': {
                'handlers': ['file', 'console'],
                'level': 'INFO',
                'propagate': True,
            },
        },
    }
    
    # Security settings for executable
    DEBUG = False
    ALLOWED_HOSTS = ['localhost', '127.0.0.1']
    SECRET_KEY = 'fire-detection-exe-key-2025-secure-random-string'
    
    # Disable some features for executable
    USE_TZ = True
    USE_I18N = True
    
    print(f"🔥 Fire Detection System - Executable Mode")
    print(f"📁 Base Directory: {BASE_DIR}")
    print(f"💾 Database: {DATABASES['default']['NAME']}")
    print(f"📊 Model: {MODEL_PATH}")