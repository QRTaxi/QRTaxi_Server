from call.models import Assign
from driver.models import CustomDriver

def get_accept_status(data, driver):
    """
    수락 요청 시 해당 assign의 status를 success로 바꾸고 driver_id도 업데이트하기
    """
    assign_id = data.get('assign_id')
    accepted = data.get('accepted')
    get_assign_info = Assign.objects.get(id=assign_id)
    get_driver_info = CustomDriver.objects.get(id=driver.id)

    if accepted:
        get_assign_info.status = 'success'
        get_assign_info.driver_id = driver
        get_driver_info.is_able = False
        get_assign_info.save(update_fields=['status', 'driver_id'])
        get_driver_info.save(update_fields=['is_able'])
    return {'statusCode': 200, 'message': '기사 수락 요청 성공'}
