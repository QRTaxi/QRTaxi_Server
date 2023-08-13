from rest_framework import serializers

class CallPushTokenSerializer(serializers.Serializer):
    assign_id = serializers.CharField(max_length=10)
    push_token = serializers.CharField(max_length=256)