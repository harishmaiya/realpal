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

    def create(self, request, *args, **kwargs):
        self.request.data['sent_by'] = self.request.user.id
        serializer = self.get_serializer(data=request.data)
        self.perform_create(serializer)

    def perform_create(self, serializer):
        room_id = self.request.data.get('room')
        try:
            room = Room.objects.get(pk=room_id)
            serializer.is_valid(self)
            instance = serializer.save(sent_by=self.request.user, room=room)
            data = {
                'id': instance.id.__str__(),
                'timestamp': instance.timestamp,
                'handle': self.request.user.username,
                'message': instance.text,
                'file_name': os.path.basename(urlparse(instance.attachment.path).path) if instance.attachment else None,
                'file_link': instance.attachment.path if instance.attachment else None,
            }
            group_channel = get_room_group_channel(room_id)
            self.push_socket_update(group_channel, data)
            return Response(instance.data, status=status.HTTP_201_CREATED)

        except Room.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def push_socket_update(group_channel, data):
        Group(group_channel).send({"text": json.dumps(data)})
