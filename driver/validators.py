import re

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_password(password):
    password_reg = r"^(?=.*[A-Za-z])(?=.*\d)(?=.*[$@$!%*#?&])[A-Za-z\d$@$!%*#?&]{6,13}$"
    password_regex = re.compile(password_reg)

    if not password_regex.match(password):
        raise ValidationError("영문, 숫자, 특수문자 조합해 6자 이상, 13자 이하 입력해주세요.")

def validate_phone_num(phone_num):
    # 가운데에 하이픈이 입력한 경우
    phone_num_reg1 = r"^(01)[016789]-\d{3,4}-\d{4}$"
    # 하이픈, 공백 없이 입력한 경우
    phone_num_reg2 = r"^(01)[016789]\d{3,4}\d{4}$"

    phone_num_regex1 = re.compile(phone_num_reg1)
    phone_num_regex2 = re.compile(phone_num_reg2)

    if not phone_num_regex1.match(phone_num) and not phone_num_regex2.match(phone_num):
        raise ValidationError("전화번호 형식이 올바르지 않습니다.(ex.010-1234-5678 또는 01012345678)")

def validate_taxi_num(taxi_num):
    taxi_num_reg = r"^\D{2}\d{2}(?:\s)?[아바사자]\d{4}$"
    taxi_num_regex = re.compile(taxi_num_reg)

    if not taxi_num_regex.match(taxi_num):
        raise ValidationError("차량 번호 형식이 올바르지 않습니다.(ex. 서울00 아0000)")