from call.models import Assign
from rest_framework import exceptions

def response_status(request_status_data):
    """
    특정 assign의 status를 반환하는 서비스
    """
    try:
        assign_id = request_status_data.get('assign_id')
        get_assign_info = Assign.objects.get(id=assign_id)
        response = {"status": get_assign_info.status}
        return response
    except Assign.DoesNotExist:
        raise exceptions.NotFound("해당 assign을 찾을 수 없습니다.")