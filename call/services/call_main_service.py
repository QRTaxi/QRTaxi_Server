from qr.models import Qr
from utils.url_hashing import Hashing
from call.serializers import CallMainGetSerializer, CallMainPostSerializer
from django.utils import timezone

def get_main(hashed_qr_id: str):
    """"
    메인 화면 호출시 주소를 반환하는 서비스
    """
    qr_id = Hashing.decode(hashed_qr_id)
    get_qr_info = Qr.objects.get(id=qr_id)
    get_qr_info_serializer = CallMainGetSerializer(get_qr_info).data
    return get_qr_info_serializer

def post_main(post_main_data, hashed_qr_id: str):
    """"
    메인 화면에서 유저의 핸드폰 번호를 적을시, assign 데이터가 생성되는 서비스
    """
    qr_id = Hashing.decode(hashed_qr_id)
    post_main_data['qr_id'] = qr_id
    post_main_data['board_at'] = timezone.now()
    post_main_serializer = CallMainPostSerializer(data=post_main_data)
    post_main_serializer.is_valid(raise_exception=True)
    post_main_serializer.save()
    return post_main_serializer.data
