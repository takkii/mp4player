#!/bin/sh
echo "run start-server.sh" &

# python manage.py runserver

# Use SSL, case --port=443
waitress-serve --port=80 mp4player.wsgi:application
