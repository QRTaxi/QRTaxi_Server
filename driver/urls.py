from django.urls import path, include
from .views import UpdateDriverLocationView, DriverOperationView
app_name = 'driver'

urlpatterns = [
    path('', include('dj_rest_auth.urls')),
    path('signup/', include('dj_rest_auth.registration.urls')),
    path('update_location/', UpdateDriverLocationView.as_view()),
    path('operation/', DriverOperationView.as_view()),
]