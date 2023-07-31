from rest_framework import serializers
from qr.models import QrImage

class QrImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = QrImage
        fields = "__all__"