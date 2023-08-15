from rest_framework import serializers
from call.models import Assign
from driver.models import CustomDriver

class CallSuccessDriverInfoSerializer(serializers.ModelSerializer):
    driver_phone = serializers.CharField(source='phone_num', read_only=True)
    class Meta:
        model = CustomDriver
        fields = ("id" ,"name", "taxi_num", "car_type", "driver_phone")

class CallSuccessGetSerializer(serializers.ModelSerializer):
    driver_id = CallSuccessDriverInfoSerializer()

    class Meta:
        model = Assign
        fields = ("id", "driver_id",)