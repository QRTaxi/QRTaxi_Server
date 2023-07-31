from rest_framework import serializers
from qr.models.qr_image import QrImage

class QrImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = QrImage
        fields = "__all__"