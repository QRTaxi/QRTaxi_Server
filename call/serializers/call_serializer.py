from rest_framework import serializers
from qr.models import Qr

class CallMainGetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Qr
        fields = ('place', 'description')