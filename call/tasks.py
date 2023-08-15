import time

from asgiref.sync import async_to_sync
from call.models import Assign
from celery import shared_task
from channels.layers import get_channel_layer
from driver.models import CustomDriver
from driver.services import get_nearest_drivers
from qr.models import Qr
from utils.redis_utils import get_redis_connection

def check_response(assign_id, driver_id):
    """
    assign db 내에 status가 success로 바뀌었는지 응답 체크하는 로직
    """
    try:
        assign = Assign.objects.get(id=assign_id)
        if assign.status == "cancel":
            return "cancel"
        if assign.driver_id:
            return assign.status == "success" if assign.driver_id.id == driver_id else False
        else:
            return False
    except Assign.DoesNotExist:
        return None
    
def check_already_driver(driver_id, assign_id, redis_conn):
    key = f"assign_set_{assign_id}"
    is_exist_in_set = redis_conn.sismember(key, driver_id)
    if not is_exist_in_set:
        return False
    else:
        return True
    
@shared_task
def assign_driver_to_request(assign_id, qr_id):
    """
    가까운 기사 10분에게 차례대로 메시지를 보내는 로직
    """
    channel_layer = get_channel_layer()
    redis_conn = get_redis_connection(db_select=1)

    qr = Qr.objects.get(id=qr_id)
    user_longitude = qr.longitude
    user_latitude = qr.latitude
    
    retry_count = 0
    max_retries = 11

    while retry_count <= max_retries:
        driver_id_list = get_nearest_drivers(user_latitude, user_longitude)

        key = f'assign_{assign_id}'
        redis_conn.delete(key)
        redis_conn.rpush(key, *driver_id_list)
        retry_count += 1

        if redis_conn.llen(key) == 0 and retry_count == max_retries:
            get_assign_info = Assign.objects.get(id=assign_id)
            get_assign_info.status = 'failed'
            get_assign_info.save(update_fields=['status'])
            return "Not accepted"

        if redis_conn.llen(key) == 0:
            if retry_count == max_retries:
                continue
            time.sleep(2)
            continue

        for driver_id in driver_id_list:
            if retry_count > 1:
                if check_already_driver(driver_id, assign_id, redis_conn):
                    continue

            if int(redis_conn.lindex(key, 0)) != driver_id:
                continue

            driver = CustomDriver.objects.get(id=driver_id)
            if not driver.is_able:
                redis_conn.lpop(key)
                continue

            async_to_sync(channel_layer.group_send)(
                "drivers",
                {
                    "type": "send_message",
                    "driver_id": driver_id,
                    "assign_id": assign_id,
                },
            )
            # 지금은 테스트용으로 확인하느라 5초로 설정해두었습니다.
            for _ in range(5):
                result = check_response(assign_id, driver_id)
                if result == "cancel":
                    return "Assign already canceled"
                elif result is None:
                    return "Error occurred"
                elif result:
                    return "Accepted"
                time.sleep(1)
            redis_conn.lpop(key)
            redis_conn.sadd(f"assign_set_{assign_id}", driver_id)

