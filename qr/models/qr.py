from django.db import models

class Qr(models.Model):
    place = models.CharField(verbose_name="큐알 장소", max_length=50)
    longitude = models.FloatField(verbose_name="경도")
    latitude = models.FloatField(verbose_name="위도")
    map_image = models.ImageField(verbose_name="장소 이미지")