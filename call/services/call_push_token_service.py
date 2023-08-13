from call.serializers import CallPushTokenSerializer
from .push_token_redis import set_push_token_to_redis

def get_push_token(request_push_token_data):
    """
    push token을 받고, redis에 "assign:{assign_id}: {token}" 으로 저장하는 service
    """
    push_token_serializer = CallPushTokenSerializer(data=request_push_token_data)
    push_token_serializer.is_valid(raise_exception=True)
    push_token_data = push_token_serializer.data 
    assign_id = push_token_data.get('assign_id')
    push_token = push_token_data.get('push_token')
    set_push_token_to_redis(assign_id, push_token)
