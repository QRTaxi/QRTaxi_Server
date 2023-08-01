from qr.models import Qr
from utils.url_hashing import Hashing
from call.serializers import CallMainGetSerializer

def get_main(hashed_qr_id):
    """"
    메인 화면 호출시 주소를 반환하는 서비스
    """
    qr_id = Hashing.decode(hashed_qr_id)
    get_qr_info = Qr.objects.get(id=qr_id)
    get_qr_info_serializer = CallMainGetSerializer(get_qr_info).data
    return get_qr_info_serializer