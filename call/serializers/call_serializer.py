from rest_framework import serializers
from qr.models import Qr
from call.models import Assign
import re
from django.core.exceptions import ValidationError

class CallMainGetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Qr
        fields = ('place', 'description')


class CallMainPostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Assign
        fields = "__all__"
    
    def validate_user_phone(self, user_phone):
        # 가운데에 하이픈이 입력한 경우
        phone_num_reg1 = r"^(01)[016789]-\d{3,4}-\d{4}$"
        # 하이픈, 공백 없이 입력한 경우
        phone_num_reg2 = r"^(01)[016789]\d{3,4}\d{4}$"

        phone_num_regex1 = re.compile(phone_num_reg1)
        phone_num_regex2 = re.compile(phone_num_reg2)

        if not phone_num_regex1.match(user_phone) and not phone_num_regex2.match(user_phone):
            raise serializers.ValidationError("전화번호 형식이 올바르지 않습니다.(ex.010-1234-5678 또는 01012345678)")
        
        return user_phone