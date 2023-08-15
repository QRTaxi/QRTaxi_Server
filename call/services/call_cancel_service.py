from call.models import Assign
from driver.models import CustomDriver
from rest_framework import exceptions

def cancel_call(cancel_call_data):
    """
    특정 assign의 call status를 cancel로 바꾸는 서비스
    """
    try:
        assign_id = cancel_call_data.get('assign_id')
        get_assign_info = Assign.objects.get(id=assign_id)
        get_assign_info.status = 'cancel'
        get_assign_info.save(update_fields=['status'])
        if get_assign_info.driver_id is not None:
            driver = get_assign_info.driver_id
            get_driver_info = CustomDriver.objects.get(id=driver.id)
            get_driver_info.is_able = True
            get_driver_info.save(update_fields=['is_able'])
    except Assign.DoesNotExist:
        raise exceptions.NotFound("해당 데이터를 찾을 수 없습니다.")