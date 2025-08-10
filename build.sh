#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt

# Create necessary directories
mkdir -p static/images/team
mkdir -p static/favicon

python manage.py collectstatic --no-input
python manage.py migrate 