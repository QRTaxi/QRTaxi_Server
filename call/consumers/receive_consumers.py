from asgiref.sync import async_to_sync
from channels.generic.websocket import JsonWebsocketConsumer


class DriverConsumer(JsonWebsocketConsumer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.group_name = "drivers"

    def connect(self):
        async_to_sync(self.channel_layer.group_add)(self.group_name, self.channel_name)
        self.accept()

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(self.group_name, self.channel_name)

    def send_message(self, event):
        driver_id = event['driver_id']
        assign_id = event['assign_id']
        type = event['type']

        self.send_json({
            'assign_id': assign_id,
            'driver_id': driver_id,
            'type': type,
        })

    def cancel(self, event_dict):
        self.send_json(event_dict)
