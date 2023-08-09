#!/bin/bash
python manage.py collectstatic --no-input
celery -A hackathon worker --loglevel=info & 
daphne -b 0.0.0.0 -p 8000 hackathon.asgi:application