from django.db import models
from qr.models import Qr
from driver.models import CustomDriver

class Assign(models.Model):
    STATUS_CHOICES = (
        ('waiting', '배정중'),
        ('success', '배정완료'),
        ('riding', '탑승완료'),
        ('finish', '운행종료'),
        ('cancel', '취소'),
    )
    qr_id = models.ForeignKey(Qr, on_delete=models.CASCADE, verbose_name="큐알")
    driver_id = models.ForeignKey(CustomDriver, on_delete=models.CASCADE, verbose_name="기사님", null=True)
    user_phone = models.CharField(verbose_name="손님 전화번호", max_length=20)

    status = models.CharField(choices=STATUS_CHOICES, default='waiting', max_length=10)
    board_at = models.DateTimeField(auto_now=True)