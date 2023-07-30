from dj_rest_auth.registration.serializers import RegisterSerializer
from allauth.account.adapter import get_adapter
from rest_framework import serializers

class CustomRegisterSerializer(RegisterSerializer):
    name = serializers.CharField(required=True, max_length=10)
    phone_num = serializers.CharField(required=True, max_length=20)
    taxi_num = serializers.CharField(required=True, max_length=20)
    birth = serializers.DateField()


    def get_cleaned_data(self):
        data = super().get_cleaned_data()
        data["name"] = self.validated_data.get("name", "")
        data["phone_num"] = self.validated_data.get("phone_num", "")
        data["taxi_num"] = self.validated_data.get("taxi_num", "")
        data["birth"] = self.validated_data.get("birth", "")

        return data

    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        user.username = self.cleaned_data.get('username')
        user.name = self.cleaned_data.get('name')
        user.phone_num = self.cleaned_data.get('phone_num')
        user.taxi_num = self.cleaned_data.get('taxi_num')
        user.birth = self.cleaned_data.get('birth')
        user.save()
        adapter.save_user(request, user, self)
        return user