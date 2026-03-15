#!/usr/bin/env bash
# exit on error
set -o errexit

# Install dependencies
pip install -r requirements.txt

# Collect static files
python Fire_detector/manage.py collectstatic --no-input

# Run migrations
python Fire_detector/manage.py migrate