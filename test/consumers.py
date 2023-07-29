from channels.generic.websocket import WebsocketConsumer, JsonWebsocketConsumer
import json
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
    groups = ["liveblog"]

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