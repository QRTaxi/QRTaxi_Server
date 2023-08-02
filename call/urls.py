from django.urls import path
from call.views import CallMainView
app_name = 'call'

urlpatterns = [
    path("wstest/<str:post_pk>/", views.liveblog_index),
    path('main/<str:hashed_qr_id>', CallMainView.as_view()),
]