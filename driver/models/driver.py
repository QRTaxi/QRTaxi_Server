from django.db import models
from django.contrib.auth.models import AbstractUser
from .time import TimestampedModel

class CustomDriver(AbstractUser, TimestampedModel):
  REQUIRED_FIELDS = []
  username = models.CharField(max_length=255, unique=True)
  name = models.CharField(max_length=10)
  phone_num = models.CharField(max_length=20)
  taxi_num = models.CharField(max_length=20, unique=True)
  birth = models.DateField(null=True)
  is_running = models.BooleanField(default=False)
