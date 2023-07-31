from django.urls import path
from qr.views import PlaceView
from qr.views import QrImageView
app_name = 'qr'

urlpatterns = [
    path('makeplace/', PlaceView.as_view()),
    path('makeqrimage/', QrImageView.as_view()),
]