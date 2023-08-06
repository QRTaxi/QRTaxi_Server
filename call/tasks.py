import time

from asgiref.sync import async_to_sync
from call.models import Assign
from celery import shared_task
from channels.layers import get_channel_layer
from driver.models import CustomDriver
from driver.services import get_nearest_drivers
from qr.models import Qr

def check_response(assign_id, driver_id):
    """
    assign db 내에 status가 success로 바뀌었는지 응답 체크하는 로직
    """
    try:
        assign = Assign.objects.get(id=assign_id)
        if assign.driver_id:
            return assign.status == "success" if assign.driver_id.id == driver_id else False
        else:
            return False
    except Assign.DoesNotExist:
        return None

@shared_task
def assign_driver_to_request(assign_id, qr_id):
    """
    가까운 기사 10분에게 차례대로 메시지를 보내는 로직
    """
    channel_layer = get_channel_layer()

    qr = Qr.objects.get(id=qr_id)
    user_longitude = qr.longitude
    user_latitude = qr.latitude
    driver_id_list = get_nearest_drivers(user_latitude, user_longitude)


    for driver_id in driver_id_list:
        driver = CustomDriver.objects.get(id=driver_id)
        if not driver.is_able:
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
            if result is None:
                return "Error occurred"
            elif result:
                return "Accepted"
            time.sleep(1)

    return "Not accepted"
