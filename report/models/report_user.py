from django.db import models
from qr.models import Qr
from driver.models import CustomDriver
from call.models import Assign

class ReportUser(models.Model):
    driver_id = models.ForeignKey(CustomDriver, on_delete=models.CASCADE, verbose_name="신고한 기사님")
    assign_id = models.ForeignKey(Assign, on_delete=models.CASCADE, verbose_name="신고당한 배정")
    report_time = models.DateTimeField(auto_now_add=True)
    contents = models.TextField(help_text="신고 내용을 작성해주세요.", blank=True)