from django.urls import path
from call.views import CallMainView, CallSuccessView, CallCancelView, ReceiveStatusView, ReceiveMainView, CallRidingView, CallFinishView, CallRequestStatusView
from test.views import liveblog_index
app_name = 'call'

urlpatterns = [
    path("wstest/<str:post_pk>/", liveblog_index),
    path('main/<str:hashed_qr_id>', CallMainView.as_view()),
    path('cancel/', CallCancelView.as_view()),
    path('status/', CallRequestStatusView.as_view()),
    path('success/<str:hashed_assign_id>', CallSuccessView.as_view()),
    path('receive/', ReceiveStatusView.as_view()),
    path('<int:assign_id>/', ReceiveMainView.as_view()),
    path('<int:assign_id>/riding/', CallRidingView.as_view()),
    path('<int:assign_id>/finish/', CallFinishView.as_view()),
]

