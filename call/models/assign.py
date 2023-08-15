from django.db import models
from qr.models import Qr
from driver.models import CustomDriver
from django.db.models.signals import post_save
from call.mixins import ChannelLayerGroupSendMixin
from .assign_signals import websocket_message, send_push_notification

class Assign(ChannelLayerGroupSendMixin, models.Model):
    STATUS_CHOICES = (
        ('waiting', '배정중'),
        ('success', '배정완료'),
        ('riding', '탑승완료'),
        ('failed', '배정실패'),
        ('finish', '운행종료'),
        ('cancel', '취소'),
    )
    qr_id = models.ForeignKey(Qr, on_delete=models.CASCADE, verbose_name="큐알")
    driver_id = models.ForeignKey(CustomDriver, on_delete=models.CASCADE, verbose_name="기사님", null=True)
    user_phone = models.CharField(verbose_name="손님 전화번호", max_length=20)

    status = models.CharField(choices=STATUS_CHOICES, default='waiting', max_length=10)
    board_at = models.DateTimeField(auto_now=True)

    @property
    def call_group_name(self):
        return self.make_call_group_name(call=self)

    @staticmethod
    def make_call_group_name(assign_pk=None):
        return f"call-{assign_pk}"
    
def call__on_post_save(instance: Assign, created: bool, **kwargs):
    websocket_message(instance, created)
    send_push_notification(instance)

post_save.connect(
    call__on_post_save,
    sender=Assign,
    dispatch_uid="call__on_post_save",
)
