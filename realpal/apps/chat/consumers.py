import json
import logging

from channels import Group

from realpal.apps.chat.models import Room, Message
from realpal.users.constants import AGENT_USER, CLIENT_USER
from realpal.users.models import User

from channels.auth import channel_session_user_from_http, channel_session_user
from django.utils import timezone

from realpal.apps.chat.models import Room
from realpal.apps.users.constants import AGENT_USER, CLIENT_USER

logger = logging.getLogger(__name__)

USER_ONLINE = 1
USER_OFFLINE = 2


def get_user_chat_status_message(username, status):
    if status == USER_ONLINE:
        message = 'User: {} has joined the chat-room'.format(username)
    else:
        message = 'User: {} has left the chat-room'.format(username)
    user_status_message = {
        'timestamp': timezone.now().strftime('%c'),
        'handle': 'Chat Room Bot',
        'message': message
    }
    return user_status_message


def send_user_chat_status(group, username, status):
    user_status_message = get_user_chat_status_message(username, status)
    Group(group).send(
        {
            "text": json.dumps(user_status_message)
        }
    )


def channel_added_logger(reply_channel, group):
    logger.debug(
        'Added reply channel: [{}] to group: {}'.format(
            reply_channel, group
        )
    )


@channel_session_user_from_http
def ws_connect(message, room_id):
    message.reply_channel.send({"accept": True})
    user = message.user
    if user.is_authenticated:
        message.channel_session["username"] = user.username
        message.channel_session["user_id"] = user.id
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
                    send_user_chat_status(group_name, user.username, USER_ONLINE)
                    channel_added_logger(message.reply_channel, message.channel_session.get('group_name'))
                else:
                    Group(group_name).add(message.reply_channel)
                    send_user_chat_status(group_name, user.username, USER_ONLINE)
                    channel_added_logger(message.reply_channel, message.channel_session.get('group_name'))
            elif user.user_type == CLIENT_USER:
                if room.client == user:
                    Group(group_name).add(message.reply_channel)
                    send_user_chat_status(group_name, user.username, USER_ONLINE)
                    channel_added_logger(message.reply_channel, message.channel_session.get('group_name'))
                else:
                    logger.debug('Access denied for user {} on room {}'.format(user, room))
                    message.reply_channel.send(
                        {
                            'close': True,
                            'text': 'Access denied for user {} on room {}'.format(user, room),
                        }
                    )
        except Room.DoesNotExist:
            logger.debug('Requested room not found')
            message.reply_channel.send(
                {
                    'close': True,
                    'text': 'Requested room {} not found'.format(room_id),
                }
            )
    else:
        logger.debug('Unauthenticated user')
        message.reply_channel.send(
            {
                'close': True,
                'text': 'Unauthenticated user',
            }
        )


@channel_session_user
def ws_receive(message):
    incoming = json.loads(message['text'])
    handle = message.channel_session.get('username')
    msg = incoming.get('message', 'Error Getting Message')
    data = {
        'timestamp': timezone.now().strftime('%c'),
        'handle': handle if handle else 'Anonymous',
        'message': msg
    }
    room = Room.objects.get(pk=message.channel_session.get('room_id'))
    user = User.objects.get(pk=message.channel_session.get('user_id'))
    Message.objects.create(
        room=room,
        sent_by=user,
        text=msg
    )
    Group(message.channel_session['group_name']).send({'text': json.dumps(data)})


@channel_session_user
def ws_disconnect(message):
    user = message.channel_session.get('username')
    send_user_chat_status(message.channel_session['group_name'], user, USER_OFFLINE)

    Group(message.channel_session['group_name']).discard(message.reply_channel)
    logger.debug(
        'Removed reply channel: [{}] from group: {}'.format(
            message.reply_channel,
            message.channel_session['group_name']
        )
    )
