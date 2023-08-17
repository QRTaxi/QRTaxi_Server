from firebase_admin import messaging
import firebase_admin

def websocket_message(instance, created: bool):
    from . import Assign

    if created:
        message_type = "waiting"
    else:
        if instance.status in ('success', 'riding', 'failed', 'finish', 'cancel'):
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
    
    if instance.status == 'cancel' and instance.driver_id:
        message_type = "cancel"
        instance.channel_layer_group_send(
            "drivers",
            {
                "assign_id": assign_pk,
                "driver_id": instance.driver_id.id,
                "type": message_type,
            }
        )

def send_push_notification(instance):
    from call.services import get_push_token_from_redis

    registration_token = get_push_token_from_redis(instance.pk)

    messages = {
        'waiting': '택시를 기다리는 중이에요.',
        'success': '택시가 배정되었어요!',
        'riding': '택시에 탑승하였어요.',
        'failed': '택시 배정에 실패하였어요.',
        'finish': '운행이 종료되었어요. 또 이용해주세요!',
        'cancel': '택시 요청이 취소되었어요.'
    }

    body = messages.get(instance.status, '알 수 없는 상태에요.')
    message = messaging.Message(
        notification = messaging.Notification(
            title='큐택 택시 정보 알림',
            body=body
        ),
        data = {
            'status': instance.status
        },
        token=registration_token,
    )
    if instance.status == "failed":
        app = firebase_admin.get_app('celery_app')
    else:
        app = firebase_admin.get_app('asgi_app')
    
    response = messaging.send(message, app=app)
    print('Successfully sent message:', response)