from django.db import models
from qr.models import Qr
from driver.models import CustomDriver
from django.db.models.signals import post_save, post_delete
from call.mixins import ChannelLayerGroupSendMixin

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

def websocket_message(instance: Assign, created: bool):
    if created:
        message_type = "waiting"
    else:
        if instance.status in ('success', 'riding', 'failed', 'finish', 'cancel'):
            message_type = instance.status
        else:
            message_type = "error"
            
    assign_pk = instance.pk

    instance.channel_layer_group_send(
        Assign.make_call_group_name(assign_pk),
        {
        "type": message_type,
        "assign_id": assign_pk,
    })
 
def call__on_post_save(instance: Assign, created: bool, **kwargs):
    websocket_message(instance, created)
    
post_save.connect(
    call__on_post_save,
    sender=Assign,
    dispatch_uid="call__on_post_save",
)
