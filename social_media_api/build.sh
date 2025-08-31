#!/usr/bin/env bash
set -o errexit

# cd social_media_api

pip install -r requirements.txt

python manage.py collectstatic --no-input

python manage.py migrate