from call.models import Assign

def riding_call(assign_id):
    """
    특정 assign의 call status를 riding으로 바꾸는 서비스
    """
    try:
        get_assign_info = Assign.objects.get(id=assign_id)
        get_assign_info.status = 'riding'
        get_assign_info.save(update_fields=['status'])
        return {'statusCode': 200, "message": "손님이 탑승을 완료하였습니다."}
    except Assign.DoesNotExist:
        return {"statusCode": 404, "message": "해당 배정정보가 없습니다."}