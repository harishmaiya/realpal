import json
import logging

from channels.auth import channel_session_user_from_http, channel_session_user
from channels import Group
from django.utils import timezone

from realpal.apps.chat.models import Room, Message
from realpal.users.constants import AGENT_USER, CLIENT_USER

logger = logging.getLogger(__name__)


@channel_session_user_from_http
def ws_connect(message, room_id):
    message.reply_channel.send({"accept": True})
    user = message.user
    if user.is_authenticated:
        message.channel_session["username"] = user.username
        try:
            room = Room.objects.get(pk=room_id)
            group_name = "Room_{}".format(room.id)
            message.channel_session["room_id"] = room.id
            message.channel_session["group_name"] = group_name
            if user.user_type == AGENT_USER:
                if room.agent is None:
                    room.agent = user
                    room.save()
                    Group(group_name).add(message.reply_channel)
                elif room.agent == user:
                    Group(group_name).add(message.reply_channel)
                else:
                    logger.debug('Access denied for user {} on room {}'.format(user, room))
                    return
            elif user.user_type == CLIENT_USER:
                if room.client == user:
                    Group(group_name).add(message.reply_channel)
                else:
                    logger.debug('Access denied for user {} on room {}'.format(user, room))
                    return
        except Room.DoesNotExist:
            print('Requested room not found')
            logger.debug('Requested room not found')
            return
    else:
        print('Unauthenticated user')
        logger.debug('Unauthenticated user')
        return


@channel_session_user
def ws_receive(message):
    incoming = json.loads(message['text'])
    handle = message.channel_session["username"]
    msg = incoming.get('message', 'Error Getting Message')

    logger.debug('Incoming message: ', handle, 'msg:', msg)

    data = {
        'timestamp': timezone.now().strftime('%c'),
        'handle': handle if handle else 'Anonymous',
        'message': msg
    }

    Group(message.channel_session["group_name"]).send({
        "text": json.dumps({
            "text": data
        }),
    })


@channel_session_user
def ws_disconnect(message):
    try:
        Group(message.channel_session["group_name"]).discard(message.reply_channel)
    except KeyError:
        pass
