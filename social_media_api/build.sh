#!/usr/bin/env bash
set -o errexit

# cd social_media_api

pip install -r requirements.txt

python manage.py collectstatic --no-input

# Apply migrations for the accounts app first to create the custom user table
python manage.py migrate accounts

# Apply all other migrations
python manage.py migrate --no-input