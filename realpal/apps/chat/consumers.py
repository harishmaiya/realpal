from channels.auth import channel_session_user_from_http, channel_session_user
from channels import Group
import json
import logging
from realpal.apps.chat.models import Room, Message


log = logging.getLogger(__name__)


@channel_session_user_from_http
def ws_connect(message):
    pass


@channel_session_user
def ws_receive(message):
    pass


@channel_session_user
def ws_disconnect(message):
    pass
