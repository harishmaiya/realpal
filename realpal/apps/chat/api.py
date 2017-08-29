import logging
import json
import os
from urllib.parse import urlparse

from channels import Group
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from realpal.apps.chat.models import Message
from realpal.apps.chat.serializers import MessageSerializer
from realpal.apps.chat.consumers import get_room_group_channel
from realpal.apps.chat.models import Room

logger = logging.getLogger(__name__)


class MessageCreateAPIView(CreateAPIView):
    """
    Creates a new message object with a file attachment

    Returns on the socket

        {
            'id': "id",
            'sent_by':'user_id',
            'room':"room_id",
            'text':message.txt,
            'file_name': message.attachment,
            'file_link': message.attachment.path
        }
    """
    model = Message
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated, ]

    def post(self, request, *args, **kwargs):
        room_id = self.request.data.get('room')
        try:
            room = Room.objects.get(pk=room_id)
            self.request.data['room'] = room_id
            self.request.data['sent_by'] = self.request.user.id
            return super().post(request, *args, **kwargs)
        except Room.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def push_socket_update(group_channel, data):
        Group(group_channel).send({"text": json.dumps(data),})
