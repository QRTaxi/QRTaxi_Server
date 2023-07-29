from django.db import models
from qr.models import Qr
from driver.models import CustomDriver
from call.models import Assign

class ReportDriver(models.Model):
    assign_id = models.ForeignKey(Assign, on_delete=models.CASCADE, verbose_name="신고한 유저")
    driver_id = models.ForeignKey(CustomDriver, on_delete=models.CASCADE, verbose_name="신고당한 기사님")
    report_time = models.DateTimeField(auto_now_add=True)