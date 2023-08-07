from django.urls import path, include
from .views import UpdateDriverLocationView, DriverOperationView, CustomLoginView, CustomLogoutView, CustomRegisterView
app_name = 'driver'

urlpatterns = [
    path('login/', CustomLoginView.as_view()),
    path('logout/', CustomLogoutView.as_view()),
    path('signup/', CustomRegisterView.as_view()),
    path('update_location/', UpdateDriverLocationView.as_view()),
    path('operation/', DriverOperationView.as_view()),
    path('an/', include('dj_rest_auth.urls')),
]