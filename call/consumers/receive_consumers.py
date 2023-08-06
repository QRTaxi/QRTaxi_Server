from asgiref.sync import async_to_sync
from call.models import Assign
from driver.models import CustomDriver
from channels.generic.websocket import JsonWebsocketConsumer


class DriverConsumer(JsonWebsocketConsumer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.group_name = "drivers"

    def connect(self):
        async_to_sync(self.channel_layer.group_add)(self.group_name, self.channel_name)
        self.accept()

    def receive_json(self, content, **kwargs):
        driver_id = content.get('driver_id')
        assign_id = content.get('assign_id')
        accepted = content.get('accepted')
        if accepted:
            Assign.objects.filter(id=assign_id).update(driver_id=driver_id, status='success')
            CustomDriver.objects.filter(id=driver_id).update(is_able=False)

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(self.group_name, self.channel_name)

    def send_message(self, event):
        driver_id = event['driver_id']
        assign_id = event['assign_id']

        self.send_json({
            'driver_id': driver_id,
            'assign_id': assign_id,
        })
