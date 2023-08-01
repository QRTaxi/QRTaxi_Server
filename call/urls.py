from django.urls import path
from test import views
app_name = 'call'

urlpatterns = [
    path("wstest/<str:post_pk>/", views.liveblog_index),
]