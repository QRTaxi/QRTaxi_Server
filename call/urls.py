from django.urls import path
from call.views import CallMainView
from test.views import liveblog_index
app_name = 'call'

urlpatterns = [
    path("wstest/<str:post_pk>/", liveblog_index),
    path('main/<str:hashed_qr_id>', CallMainView.as_view()),
]