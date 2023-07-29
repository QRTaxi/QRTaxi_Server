from django.db import models

class TimestampedModel(models.Model):
    # 수정된 날짜를 기록
    updated_at = models.DateTimeField(auto_now=True)
    # 탈퇴된 날짜를 기록
    withdraw_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
