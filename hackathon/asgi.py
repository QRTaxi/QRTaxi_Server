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
import test.routing
from call.routings import call_routing
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hackathon.settings')

django_asgi_app = get_asgi_application()

application = ProtocolTypeRouter({
    "http": django_asgi_app,
    "websocket": URLRouter(
        test.routing.websocket_urlpatterns + call_routing.websocket_urlpatterns,
    )
})