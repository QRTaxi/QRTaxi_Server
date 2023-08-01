from django.urls import path, re_path
from . import views


urlpatterns = [
   path('', views.TestView.as_view()),
   path("liveblog/<str:post_pk>/", views.liveblog_index),
]

