from django.urls import path, include
from mypage.views.mypage_profile import UserDetailView
from mypage.views.mypage_assign_list import DriverAssignmentsView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

app_name = 'driver'

urlpatterns = [
    path('', include('dj_rest_auth.urls')),
    path('signup/', include('dj_rest_auth.registration.urls')),
    path('<int:pk>/mypage/', UserDetailView.as_view(), name='mypage'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('<int:pk>/mypage/assignment', DriverAssignmentsView.as_view(), name='driver_assignments'),
]