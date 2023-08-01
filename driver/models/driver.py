from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from driver.managers import UserManager

from .time import TimestampedModel


# AbstractBaseUser -> password, last_login, is_active
class CustomDriver(AbstractBaseUser, PermissionsMixin, TimestampedModel):
    username = models.CharField(
        verbose_name="username",
        max_length=50,
        unique=True,
        error_messages={"unique": "이미 존재하는 아이디입니다."},
        )

    name = models.CharField(max_length=10, null=False, blank=False)
    phone_num = models.CharField(max_length=20, null=False, blank=False)

    taxi_num = models.CharField(
        verbose_name="taxi_num",
        max_length=20,
        unique=True,
        error_messages={"unique": "이미 존재하는 차 번호입니다."},
        )

    birth = models.DateField(null=True)
    car_type = models.CharField(max_length=20, null=False, blank=False)
    is_able = models.BooleanField(default=False)
    profile_image = models.CharField(max_length=256, null=True, blank=True)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ["password", "name", "phone_num", "taxi_num", "car_type"]

    objects = UserManager()

    def __str__(self):
        return self.username