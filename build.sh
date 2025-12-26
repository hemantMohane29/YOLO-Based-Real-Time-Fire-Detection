#!/usr/bin/env bash
# exit on error
set -o errexit

# Install dependencies
pip install -r requirements.txt

# Navigate to the Django project directory
cd Fire_detector

# Collect static files
python manage.py collectstatic --no-input

# Run migrations
python manage.py migrate