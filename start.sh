#!/bin/bash
python manage.py collectstatic --no-input
daphne -b 0.0.0.0 -p 8000 hackathon.asgi:application