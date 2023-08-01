from channels.generic.websocket import WebsocketConsumer, JsonWebsocketConsumer
import json
from asgiref.sync import async_to_sync
from .models import Post

class EchoConsumer(WebsocketConsumer):
    def receive(self, text_data=None, bytes_data=None):
        obj = json.loads(text_data)
        print("수신: ", obj)

        json_string = json.dumps({
            "content": obj["content"],
            "user": obj["user"]
        })
        self.send(json_string)

class LiveblogConsumer(JsonWebsocketConsumer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.group_name = ""

    def connect(self):
        post_pk = self.scope["url_route"]["kwargs"]["post_pk"]
        self.group_name = Post.make_call_group_name(post_pk)

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
    
    def liveblog_post_waiting(self, event_dict):
        self.send_json(event_dict)

    def liveblog_post_success(self, event_dict):
        self.send_json(event_dict)
    
    def liveblog_post_riding(self, event_dict):
        self.send_json(event_dict)

    def liveblog_post_finish(self, event_dict):
        self.send_json(event_dict)

    def liveblog_post_cancel(self, event_dict):
        self.send_json(event_dict)

    def liveblog_post_deleted(self, event_dict):
        self.send_json(event_dict)