from rest_framework import serializers
from qr.models.qr import Qr

class PlaceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Qr
        fields = "__all__"