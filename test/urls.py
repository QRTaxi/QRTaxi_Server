from django.urls import path, re_path
from . import views


urlpatterns = [
   path('', views.TestView.as_view()),
   path("liveblog/", views.liveblog_index),
]

