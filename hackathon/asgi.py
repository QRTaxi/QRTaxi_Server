"""
ASGI config for hackathon project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""
import os
from channels.routing import URLRouter
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter
from call.routings import call_routing
import firebase_admin
from firebase_admin import credentials
from decouple import config
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hackathon.settings')

cred_path = config("FIRE_BASE_JSON_KEY_PATH")
cred = credentials.Certificate(cred_path)
firebase_admin.initialize_app(cred, name='asgi_app')

django_asgi_app = get_asgi_application()

application = ProtocolTypeRouter({
    "http": django_asgi_app,
    "websocket": URLRouter(
        call_routing.websocket_urlpatterns
    )
})