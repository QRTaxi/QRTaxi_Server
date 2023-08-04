from rest_framework import serializers
from driver.models import CustomDriver
'''
class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomDriver
        fields = ['username', 'name', 'phone_num', 'taxi_num', 'birth', 'car_type', 'is_able', 'profile_image', 'is_active']
        read_only_fields = ['username', 'date_joined']

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.phone_num = validated_data.get('phone_num', instance.phone_num)
        instance.taxi_num = validated_data.get('taxi_num', instance.taxi_num)
        instance.birth = validated_data.get('birth', instance.birth)
        instance.car_type = validated_data.get('car_type', instance.car_type)
        instance.is_able = validated_data.get('is_able', instance.is_able)
        instance.profile_image = validated_data.get('profile_image', instance.profile_image)
        instance.is_active = validated_data.get('is_active', instance.is_active)
        instance.save()
        return instance
'''