import json
import tempfile

from PIL import Image
from rest_framework import status
from django.urls import reverse
from django.conf import settings
from django.core.files.storage import default_storage
from rest_framework.test import APITestCase

from realpal.apps.chat.models import Room, Message
from realpal.apps.users.models import User
from realpal.apps.users.constants import AGENT_USER, CLIENT_USER


class MessageFileUploadTest(APITestCase):
    api_url_name = 'chat:chat-file'  # url with namespace

    # Generated files path for later destruction in tear down
    saved_attachment_path = ''
    temp_file_path = ''

    def setUp(self):
        self.user = User.objects.create(
            email='test@test.com'
        )
        self.room = Room.objects.get(client=self.user).id

    def test_post(self):
        """
        saves a message with a file attachment
        """
        self.url = reverse(self.api_url_name)

        # test unauthenticated
        response = self.client.post(self.url, json.dumps({}), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        self.client.force_login(user=self.user)

        # Set the mode to binary and read so it can be decoded as binary

        image = Image.new('RGB', (100, 100))

        tmp_file = tempfile.NamedTemporaryFile(dir=settings.MEDIA_ROOT, prefix='testy', suffix='.jpeg', delete=False)
        image.save(tmp_file, format='jpeg')

        # Store generated image path for later destruction in tear down
        self.temp_file_path = tmp_file.name

        with open(tmp_file.name, 'rb') as f:
            data = {
                'attachment': f,
                'room': self.room,
                'text': 'Group Rules'
            }
            response = self.client.post(self.url, data, format='multipart')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # test if message attachment was generated in the media folder
        saved_message_attachment = Message.objects.get(room=self.room)

        self.saved_attachment_path = saved_message_attachment.attachment.path

        self.assertTrue(default_storage.exists(self.saved_attachment_path))

    def tearDown(self):
        default_storage.delete(self.saved_attachment_path)
        default_storage.delete(self.temp_file_path)
        super().tearDown()


class RoomTests(APITestCase):
    api_url_name = 'chat:update-room'

    def setUp(self):
        self.client_user = User.objects.create(
            email='client@test.com',
            username='client',
            user_type=CLIENT_USER
        )
        self.agent = User.objects.create(
            email='agent@test.com',
            username='agent',
            user_type=AGENT_USER
        )
        self.room = Room.objects.get(client=self.client_user)
        self.room.agent = self.agent
        self.room.save()

    def test_unassign_client(self):
        self.url = reverse(self.api_url_name)

        # test unauthenticated
        response = self.client.patch(self.url, data=json.dumps({}), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        self.client.force_login(user=self.agent)
        data = {
            'id': self.room.id,
            'client': self.client_user.id,
            'agent': self.agent.id
        }
        response = self.client.patch(self.url, data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
