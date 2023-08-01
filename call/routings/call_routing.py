from call.consumers import CallConsumer
from django.urls import path

websocket_urlpatterns = [
    path("ws/call/<str:assign_pk>/", CallConsumer.as_asgi()),
]