import json
import logging
import tempfile

from PIL import Image
from rest_framework import status
from django.urls import reverse
from django.conf import settings
from django.core.files.storage import default_storage
from model_mommy import mommy
from rest_framework.test import APITestCase

from realpal.apps.chat.models import Room
from realpal.apps.users.models import User


class MessageFileUploadTest(APITestCase):
    api_url_name = 'chat-file'

    def setUp(self):
        self.user = mommy.make(User)

    def test_post(self):
        """
        creates a file, optionally in a specific folder, otherwise in root folder
        """
        self.url = reverse(self.api_url_name)

        # test unauthenticated
        response = self.client.post(self.url, json.dumps({}), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        self.client.force_login(user=self.user)

        # Set the mode to binary and read so it can be decoded as binary

        image = Image.new('RGB', (100, 100))

        tmp_file = tempfile.NamedTemporaryFile(dir=settings.MEDIA_ROOT, prefix='testy', suffix='.jpeg', delete=False)
        image.save(tmp_file, format='jpeg')

        with open(tmp_file.name, 'rb') as f:
            data = {
                'attachment': f,
                'room': Room.objects.get(client=self.user).id,
                'text':'Group Rules'
            }
            response = self.client.post(self.url, data, format='multipart')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

