from django.urls import path
from call.views import CallMainView
app_name = 'call'

urlpatterns = [
    path('main/<str:hashed_qr_id>', CallMainView.as_view()),
]