from test_plus.test import TestCase

from realpal.apps.chat.models import Room


class TestUser(TestCase):

    def setUp(self):
        self.user = self.make_user()

    def test__str__(self):
        self.assertEqual(
            self.user.__str__(),
            'testuser'  # This is the default username for self.make_user()
        )

    def test_get_absolute_url(self):
        self.assertEqual(
            self.user.get_absolute_url(),
            '/users/testuser/'
        )

    def test_user_room_creation(self):
        user_room = Room.objects.get(client=self.user)
        self.assertEqual(user_room.client, self.user)
