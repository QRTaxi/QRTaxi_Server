from call.models import Assign
from driver.models import CustomDriver

def finish_call(driver, assign_id):
    """
    특정 assign의 call status를 finish로 바꾸는 서비스
    """
    try:
        get_assign_info = Assign.objects.get(id=assign_id)
        get_driver_info = CustomDriver.objects.get(id=driver.id)
        get_assign_info.status = 'finish'
        get_driver_info.is_able = True
        get_assign_info.save(update_fields=['status'])
        get_driver_info.save(update_fields=['is_able'])
        return {'statusCode': 200, "message": "손님이 하차하셨습니다."}
    except Assign.DoesNotExist:
        return {"statusCode": 404, "message": "해당 배정정보가 없습니다."}