from decouple import config

def websocket_message(instance, created: bool):
    from . import Assign
    
    if created:
        message_type = "waiting"
    else:
        if instance.status in ('success', 'riding', 'failed', 'finish'):
            message_type = instance.status
        else:
            message_type = "error"
            
    assign_pk = instance.pk

    instance.channel_layer_group_send(
        Assign.make_call_group_name(assign_pk),
        {
        "type": message_type,
        "assign_id": assign_pk,
    })

def send_push_notification(instance):
    from call.services import get_push_token_from_redis

    token = get_push_token_from_redis(instance.pk)
    push_service = ""

    messages = {
        'waiting': '택시를 기다리는 중이에요.',
        'success': '택시가 배정되었어요.',
        'riding': '택시에 탑승하였어요.',
        'failed': '택시 배정에 실패하였어요.',
        'finish': '운행이 종료되었어요.',
        'cancel': '택시 요청이 취소되었어요.'
    }
    message = messages.get(instance.status, '알 수 없는 상태에요.')
    push_service.notify_single_device(registration_id=token, message_title="큐택 상태 알림", message_body=message)
