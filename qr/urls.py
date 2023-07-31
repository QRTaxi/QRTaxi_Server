from django.urls import path
from qr.views.place_view import PlaceView
app_name = 'qr'

urlpatterns = [
    path('make/', PlaceView.as_view())
]