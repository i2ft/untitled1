from channels.routing import route
from untitled1.test_channel import ws_message
channel_routing = [
    #route("http.request", "untitled1.test_channel.http_consumer"),
    route("websocket.receive", ws_message),
]