from django.urls import path, re_path
from . import views, redis_test


urlpatterns = [
   path('', views.TestView.as_view()),
   path('update_location/', redis_test.UpdateDriverLocationView.as_view()),
   path('get_nearest_drivers/', redis_test.GetNearestDriversView.as_view()),
]

