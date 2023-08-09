from qr.models import Qr
from utils.url_hashing import Hashing
from call.serializers import CallMainGetSerializer, CallMainPostSerializer
from django.utils import timezone
from call.tasks import assign_driver_to_request
from rest_framework import exceptions

def get_main(hashed_qr_id: str):
    """"
    메인 화면 호출시 주소를 반환하는 서비스
    """
    try:
        qr_id = Hashing.decode(hashed_qr_id)
        get_qr_info = Qr.objects.get(id=qr_id)
        get_qr_info_serializer = CallMainGetSerializer(get_qr_info).data
        return get_qr_info_serializer
    except Qr.DoesNotExist:
        raise exceptions.NotFound("해당 QR데이터를 찾을 수 없습니다.")

def post_main(post_main_data, hashed_qr_id: str):
    """"
    메인 화면에서 유저의 핸드폰 번호를 적을시, assign 데이터가 생성되는 서비스
    """
    qr_id = Hashing.decode(hashed_qr_id)
    post_main_data['qr_id'] = qr_id
    post_main_data['board_at'] = timezone.now()
    post_main_serializer = CallMainPostSerializer(data=post_main_data)
    post_main_serializer.is_valid(raise_exception=True)
    saved_assign = post_main_serializer.save()
    result = post_main_serializer.data
    assign_id = result.get('id')
    result['hashed_assign_id'] = Hashing.encode(assign_id)

    # Celery를 이용하여 비동기적으로 드라이버에게 배정 요청을 보냄
    assign_driver_to_request.delay(saved_assign.id, qr_id)
    return result