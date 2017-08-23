from .consumers import (
    ws_connect, ws_receive, ws_disconnect
)
from channels import route

channel_routing = [
    route('websocket.connect', ws_connect, path=r'^/(?P<room_id>[\d]+)$'),
    route('websocket.receive', ws_receive),
    route('websocket.disconnect', ws_disconnect),
]
