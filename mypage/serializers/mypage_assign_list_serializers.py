from rest_framework import serializers
from call.models import Assign

class AssignSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assign
        fields = '__all__'
