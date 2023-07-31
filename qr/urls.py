from django.urls import path
from qr.views.place_view import PlaceView
from qr.views.qr_image_view import QrImageView
app_name = 'qr'

urlpatterns = [
    path('makeplace/', PlaceView.as_view()),
    path('makeqrimage/', QrImageView.as_view()),
]