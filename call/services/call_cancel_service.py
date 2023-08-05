from call.models import Assign
from utils.url_hashing import Hashing

def cancel_call(cancel_call_data):
    """
    특정 assign의 call status를 cancel로 바꾸는 서비스
    """
    assign_id = cancel_call_data.get('assign_id')
    get_assign_info = Assign.objects.get(id=assign_id)
    get_assign_info.status = 'cancel'
    get_assign_info.save(update_fields=['status'])
    