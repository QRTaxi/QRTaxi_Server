from rest_framework import serializers
from driver.models import CustomDriver

class CustomDriverDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomDriver
        fields = [
            "id",
            "username",
            "password",
            "name",
            "phone_num",
            "taxi_num",
            "birth",
            "is_running",
        ]
        read_only_fields = [
            "id",
            "username",
            "password",
        ]