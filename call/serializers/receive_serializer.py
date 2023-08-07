from rest_framework import serializers
from call.models import Assign

class AssignInfoSerializer(serializers.ModelSerializer):
    place = serializers.CharField(source='qr_id.place', read_only=True)
    description = serializers.CharField(source='qr_id.description', read_only=True)

    class Meta:
        model = Assign
        fields = ('user_phone', 'place', 'description')
