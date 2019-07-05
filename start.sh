#!/usr/bin/env bash

echo "... Wait 3 secs for postgres up"
sleep 3

echo "... Applying Django migrations"
python manage.py makemigrations
python manage.py migrate

echo "... Applying Django collect static"
python manage.py collectstatic --noinput --clear

echo "... Starting Django"
gunicorn config.wsgi -b 0.0.0.0:8000 --reload