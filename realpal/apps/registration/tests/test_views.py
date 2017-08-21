from django.test import Client, TestCase
from django.urls import reverse
from realpal.users.models import User, City
from realpal.users.constants import *


class RegistrationTest(TestCase):
    client = Client()

    urls = {
        'purchase_step': reverse('register:purchase-step'),
        'marital_status': reverse('register:marital-status'),
        'first_home': reverse('register:first-home'),
        'house_type': reverse('register:house-type'),
        'city': reverse('register:city'),
        'max_budget': reverse('register:max-budget'),
        'current_rent': reverse('register:current-rent'),
        'how_soon': reverse('register:how-soon'),
        'personal_profile': reverse('register:personal-profile'),
    }

    def setUp(self):
        super().setUp()

    def tearDown(self):
        super().tearDown()

    def test_get(self):
        # test to see that all pages are reachable
        for url_name in self.urls:
            response = self.client.get(self.urls[url_name])
            self.assertEqual(response.status_code, 200)

    def test_post(self):
        """
         The dictionary below contains keys which match each of the keys of self.urls above
         each of these keys contain another dictionary which will be passed as the data when
         we test posting to the matching url from self.urls
        """
        data = {
            'purchase_step': {'purchase_step': PS_DAP},
            'marital_status': {'status': SC_SI},
            'first_home': {'firsthome': True},
            'house_type': {'house_type': HT_SF, 'house_age': HA_15, 'house_cond': HC_SL},
            'city': {'preferred_city': None},
            'max_budget': {'budget': 1200.59},
            'current_rent': {'current_rent': 321.49},
            'how_soon': {'how_soon': HS_3},
        }

        'personal_profile': {
            'first_name': 'TestFirstName',
            'last_name': 'TestLastName',
            'zipcode': '10118',
            'phone_number': '+263771819478',
            'email': 'test_email@gmail.com',
            'password1': 'test_password',
            'password2': 'test_password',
        },

        # lets get the number of users before saving another
        users_before = User.objects.count()

        # test to see that all views will post correctly
        for url_name in self.urls:
            data_to_pass = dict(data[url_name])  # use dict to explicitly convert string to dictionary
            response = self.client.post(self.urls[url_name], data=data_to_pass)
            self.assertEqual(response.status_code, 302)

        # test to verify we have one more user
        self.assertEqual(User.objects.count(), users_before+1)

        # test to ensure the user we just added got the session variables
        user = User.objects.latest('id')
        self.assertEqual(user.purchase_step, data['purchase_step']['purchase_step'])
        self.assertEqual(user.status, data['marital_status']['status'])
        self.assertEqual(user.firsthome, data['first_home']['firsthome'])
        self.assertEqual(user.house_type, data['house_type']['house_type'])
        self.assertEqual(user.house_age, data['house_type']['house_age'])
        self.assertEqual(user.house_cond, data['house_type']['house_cond'])
        self.assertEqual(user.budget, data['max_budget']['budget'])
        self.assertEqual(user.current_rent, data['current_rent']['current_rent'])
        self.assertEqual(user.how_soon, data['how_soon']['how_soon'])

        self.assertEqual(user.email, data['personal_profile']['email'])
        self.assertEqual(user.zipcode, data['personal_profile']['zipcode'])
