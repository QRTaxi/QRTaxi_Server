from django.db import models
from django.db.models.signals import post_save, post_delete
from django.urls import reverse

from .mixins import ChannelLayerGroupSendMixin


class Post(ChannelLayerGroupSendMixin, models.Model):
    # CHANNEL_LAYER_GROUP_NAME = "liveblog"

    status_choices = (
        ('waiting', '배정중'),
        ('success', '배정완료'),
        ('riding', '탑승완료'),
        ('finish', '운행종료'),
        ('cancel', '취소'),
    )

    user_phone = models.CharField(max_length=200, null=True)
    status = models.CharField(max_length=50, choices=status_choices, default='waiting')
    driver = models.CharField(max_length=5, null=True)

    class Meta:
        ordering = ["-id"]

    @property
    def call_group_name(self):
        return self.make_call_group_name(call=self)

    @staticmethod
    def make_call_group_name(call_pk=None):
        return f"call-{call_pk}"

def post__on_post_save(instance: Post, created: bool, **kwargs):
    if created:
        message_type = "liveblog.post.waiting"
    else:
        if instance.status == 'success':
            message_type = "liveblog.post.success"

        elif instance.status == 'riding':
            message_type = "liveblog.post.riding"

        elif instance.status == 'finish':
            message_type = "liveblog.post.finish"
            
        else:
            message_type = "liveblog.post.cancel"

    post_pk = instance.pk
    #post_partial_url = reverse("post_partial", args=[post_id])

    instance.channel_layer_group_send(
        Post.make_call_group_name(post_pk),
        {
        "type": message_type,
        "post_id": post_pk,
        #"post_partial_url": post_partial_url,
    })


post_save.connect(
    post__on_post_save,
    sender=Post,
    dispatch_uid="post__on_post_save",
)


def post__on_post_delete(instance: Post, **kwargs):
    post_pk = instance.pk

    instance.channel_layer_group_send(
        Post.make_call_group_name(post_pk),
        {
        "type": "liveblog.post.deleted",
        "post_id": post_pk,
    })


post_delete.connect(
    post__on_post_delete,
    sender=Post,
    dispatch_uid="post__on_post_delete",
)