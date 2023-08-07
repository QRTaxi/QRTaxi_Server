from django.urls import path
from mypage.views.mypage_profile import MypageDetailView
from mypage.views.mypage_assign_list import DriverAssignmentsView


app_name = 'mypage'

urlpatterns = [
    path('<int:pk>/', MypageDetailView.as_view(), name='mypage'),
    path('<int:pk>/assignment', DriverAssignmentsView.as_view(), name='driver_assignments'),
]