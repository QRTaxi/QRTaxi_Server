from django.urls import path
from mypage.views.mypage_profile import MypageDetailView
from mypage.views.mypage_assign_list import DriverAssignmentsView


app_name = 'mypage'

urlpatterns = [
    path('', MypageDetailView.as_view(), name='mypage'),
    path('assignment/', DriverAssignmentsView.as_view(), name='driver_assignments'),
]