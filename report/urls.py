from django.urls import path
from report.views.report_driver_views import ReportDriverView
from report.views.report_user_views import ReportUserView

app_name = 'report'

urlpatterns = [
    path('driver/', ReportDriverView.as_view(), name='report_drvier'),
    path('user/', ReportUserView.as_view(), name='report_user'),
]