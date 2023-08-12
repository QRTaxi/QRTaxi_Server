from channels.generic.websocket import JsonWebsocketConsumer
from asgiref.sync import async_to_sync
from django.apps import apps

class CallConsumer(JsonWebsocketConsumer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.group_name = ""

    def connect(self):
        Assign = apps.get_model('call', 'Assign') 
        assign_pk = self.scope["url_route"]["kwargs"]["assign_pk"]
        self.group_name = Assign.make_call_group_name(assign_pk)

        async_to_sync(self.channel_layer.group_add)(
            self.group_name,
            self.channel_name,
        )
        self.accept()

    def disconnect(self, code):
        if self.group_name:
            async_to_sync(self.channel_layer.group_discard)(
                self.group_name,
                self.channel_name,
            )
    
    def waiting(self, event_dict):
        self.send_json(event_dict)

    def success(self, event_dict):
        self.send_json(event_dict)
    
    def riding(self, event_dict):
        self.send_json(event_dict)

    def failed(self, event_dict):
        self.send_json(event_dict)

    def finish(self, event_dict):
        self.send_json(event_dict)

    def cancel(self, event_dict):
        self.send_json(event_dict)

    def deleted(self, event_dict):
        self.send_json(event_dict)