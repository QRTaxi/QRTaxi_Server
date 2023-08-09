from call.consumers import CallConsumer, DriverConsumer
from django.urls import path

websocket_urlpatterns = [
    path("ws/call/receive/", DriverConsumer.as_asgi()),
    path("ws/call/<str:assign_pk>/", CallConsumer.as_asgi()),
]