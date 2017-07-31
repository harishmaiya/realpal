
'''
chat logic goes here
'''
from channels.auth import channel_session_user_from_http, channel_session_user
from channels import Group
import json
import logging
from mainapp.models import Room


log = logging.getLogger(__name__)


@channel_session_user_from_http
def ws_connect(message):
    # get the user
    user = message.user

    # if type of user is booster, we handle it differently
    if user.groups.all()[0].name == 'Booster':
        # get all orders of Booster
        for order in user.order_booster.filter(status='A'):
            label = str(order.id)[:8]
            room = Room.objects.get(label=label)
            Group(
                'chat-'+label,
                channel_layer=message.channel_layer
            ).add(message.reply_channel)
    else:
        try:
            prefix, label = message['path'].decode('ascii').strip('/').split('/')
            label = str(label[:8])
            if prefix != 'chat':
                log.debug('invalid ws path=%s', message['path'])
                return
            room = Room.objects.get(label=label)
        except ValueError:
            log.debug('invalid ws path=%s', message['path'])
            return
        except Room.DoesNotExist:
            log.debug('ws room does not exist label=%s', label)
            return

        log.debug(
            'chat connect room=%s client=%s:%s',
            room.label, message['client'][0], message['client'][1]
        )
        # Need to be explicit about the channel layer so that testability works
        # This may be a FIXME?
        Group(
            'chat-'+label,
            channel_layer=message.channel_layer
        ).add(message.reply_channel)

        message.channel_session['room'] = room.label


@channel_session_user
def ws_receive(message):
    # Look up the room from the channel session, bailing if it doesn't exist
    user = message.user
    # if type of user is booster, we handle it differently
    if user.groups.all()[0].name == 'Booster':
        # get all orders of Booster
        try:
            data = json.loads(message['text'])
            label = data['orderid'][:8]
            room = Room.objects.get(label=label)
        except:
            pass
    else:
        try:
            label = message.channel_session['room']
            room = Room.objects.get(label=label)
        except KeyError:
            log.debug('no room in channel_session')
            return
        except Room.DoesNotExist:
            log.debug('recieved message, buy room does not exist label=%s', label)
            return

    # Parse out a chat message from the content text, bailing if it doesn't
    # conform to the expected message format.
    try:
        data = json.loads(message['text'])
    except ValueError:
        log.debug("ws message isn't json text=%s", data)
        return

    if data:
        log.debug(
            'chat message room=%s handle=%s message=%s',
            room.label, data['handle'], data['message']
        )
        m = room.messages.create(**data)
        # See above for the note about Group
        Group(
            'chat-'+label, channel_layer=message.channel_layer
        ).send({'text': json.dumps(m.as_dict())})


@channel_session_user
def ws_disconnect(message):
    # get the user
    user = message.user

    # if type of user is booster, we handle it differently
    if user.groups.all()[0].name == 'Booster':
        # get all orders of Booster
        for order in user.order_booster.filter(status='A'):
            label = str(order.id)[:8]
            Group(
                'chat-'+label, channel_layer=message.channel_layer
            ).discard(message.reply_channel)
    else:
        try:
            label = message.channel_session['room']
            Room.objects.get(label=label)
            Group(
                'chat-'+label, channel_layer=message.channel_layer
            ).discard(message.reply_channel)
        except (KeyError, Room.DoesNotExist):
            pass
