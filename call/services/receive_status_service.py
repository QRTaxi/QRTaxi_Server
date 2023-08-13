from call.models import Assign
from driver.models import CustomDriver
from utils.redis_utils import get_redis_connection

def validate_driver(assign_id, driver_id):
    """
    현재 수락 요청을 보낸 기사 id와 콜요청 메시지 받은 기사와 일치하는지 확인
    """
    key = f'assign_{assign_id}'
    redis_conn = get_redis_connection()
    current_driver_id = redis_conn.lindex(key, 0)

    if current_driver_id is None:
        return False

    current_driver_id = int(current_driver_id)
    return current_driver_id == driver_id


def get_accept_status(data, driver):
    """
    수락 요청 시 해당 assign의 status를 success로 바꾸고 driver_id도 업데이트하기
    """
    assign_id = data.get('assign_id')
    accepted = data.get('accepted')
    try:
        get_assign_info = Assign.objects.get(id=assign_id)
    except Assign.DoesNotExist:
        return {'statusCode': 404, 'message': "해당 배정정보가 없습니다."}

    if not validate_driver(assign_id, driver.id):
        return {'statusCode': 400, 'message': "현재 처리 중인 기사가 아닙니다."}

    if accepted:
        if get_assign_info.status == "cancel":
            return {'statusCode': 400, 'message': "이미 취소된 배정입니다."}
        try:
            get_driver_info = CustomDriver.objects.get(id=driver.id)
        except CustomDriver.DoesNotExist:
            return {'statusCode': 404, 'message': "해당 기사님이 존재하지 않습니다."}
        get_assign_info.status = 'success'
        get_assign_info.driver_id = driver
        get_driver_info.is_able = False
        get_assign_info.save(update_fields=['status', 'driver_id'])
        get_driver_info.save(update_fields=['is_able'])
    return {'statusCode': 200}
