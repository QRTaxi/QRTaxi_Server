from rest_framework import serializers

class CheckHashingSerializer(serializers.Serializer):
    target = serializers.CharField(max_length=10)
