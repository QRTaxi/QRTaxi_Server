from allauth.account.adapter import get_adapter
from dj_rest_auth.registration.serializers import RegisterSerializer
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from driver.models import CustomDriver
from driver.validators import (validate_password, validate_phone_num,
                               validate_taxi_num)
from rest_framework import serializers
from rest_framework.validators import UniqueValidator


class CustomRegisterSerializer(RegisterSerializer):
    email = None
    password1 = serializers.CharField(required=True, validators=[validate_password])
    name = serializers.CharField(required=True, max_length=10)
    phone_num = serializers.CharField(required=True, max_length=20, validators=[validate_phone_num])
    taxi_num = serializers.CharField(required=True, max_length=20,
                                     validators=[validate_taxi_num, UniqueValidator(queryset=CustomDriver.objects.all(), message='이미 존재하는 차량번호입니다.')])
    birth = serializers.CharField(max_length=20)
    car_type = serializers.CharField(required=True, max_length=20)

    def validate(self, data):
        if data["password1"] != data["password2"]:
            raise ValidationError("비밀번호가 일치하지 않습니다.")
        return data


    def get_cleaned_data(self):
        data = super().get_cleaned_data()
        data["name"] = self.validated_data.get("name", "")
        data["phone_num"] = self.validated_data.get("phone_num", "")
        data["taxi_num"] = self.validated_data.get("taxi_num", "")
        data["birth"] = self.validated_data.get("birth", "")
        data["car_type"] = self.validated_data.get("car_type", "")

        return data

    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        user.username = self.cleaned_data.get('username')
        user.name = self.cleaned_data.get('name')
        user.phone_num = self.cleaned_data.get('phone_num')
        user.taxi_num = self.cleaned_data.get('taxi_num')
        user.birth = self.cleaned_data.get('birth')
        user.car_type = self.cleaned_data.get('car_type')
        user.save()
        adapter.save_user(request, user, self)
        return user