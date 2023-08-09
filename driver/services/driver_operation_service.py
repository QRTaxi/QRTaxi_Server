from driver.models import CustomDriver

def change_driver_able(data, driver):
    operation = data.get('operation')

    if not isinstance(operation, bool):
        return {'statusCode': 400, 'message': 'operation은 불린 값이어야 합니다.'}

    get_driver_info = CustomDriver.objects.get(id=driver.id)
    get_driver_info.is_able = operation
    get_driver_info.save(update_fields=["is_able"])

    if operation:
        return {'statusCode': 200, 'message': '기사 운행 시작'}
    else:
        return {'statusCode': 200, 'message': '기사 운행 종료'}
