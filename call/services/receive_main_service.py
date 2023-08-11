from call.models import Assign
from call.serializers import AssignInfoSerializer

def get_assign(assign_id):
    """"
    배정 정보페이지 호출 시 배정정보를 반환하는 서비스
    """
    try:
        assign = Assign.objects.get(pk=assign_id)
        serializer = AssignInfoSerializer(assign)
        return {"statusCode":200, "data":serializer.data}
    except Assign.DoesNotExist:
        return {"statusCode": 404, "message": "해당 배정정보가 없습니다."}