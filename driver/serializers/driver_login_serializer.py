from dj_rest_auth.serializers import LoginSerializer

class CustomLoginSerializer(LoginSerializer):
    email = None