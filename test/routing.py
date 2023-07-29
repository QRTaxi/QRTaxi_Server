from test.consumers import EchoConsumer, LiveblogConsumer
from django.urls import path

websocket_urlpatterns = [
    path("ws/echo/", EchoConsumer.as_asgi()),
    path("ws/liveblog/", LiveblogConsumer.as_asgi()),
]