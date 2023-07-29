from django.db import models
from .qr import Qr

class QrImage(models.Model):
    qr = models.OneToOneField(Qr, on_delete=models.CASCADE)
    qr_url = models.URLField(max_length=256)
    qr_image = models.CharField(max_length=256)