from rest_framework import serializers
from driver.models import CustomDriver

class MypageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomDriver
        fields = ['username', 'name', 'phone_num', 'car_type', 'is_able', 'profile_image', 'is_active']