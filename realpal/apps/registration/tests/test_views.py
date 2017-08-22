from django.test import Client, TestCase
from django.urls import reverse
from django.core import mail
from realpal.users.models import User, PasswordReset
from realpal.users.constants import *
from django.conf import settings


class RegistrationTest(TestCase):
    client = Client()
    client_2 = Client()

    # here we create this list of keys so we can iterate in this order, the personal profile step must be the last
    keys = ('purchase_step', 'marital_status', 'first_home', 'house_type', 'city', 'max_budget', 'current_rent',
            'how_soon', 'personal_profile')

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

    def test_get(self):
        # test to see that all pages are reachable
        for url_name in self.keys:
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
            'city': {'preferred_city': ''},
            'max_budget': {'budget': 1200.59},
            'current_rent': {'current_rent': 321.49},
            'how_soon': {'how_soon': HS_3},
            'personal_profile': {
                'first_name': 'TestFirstName',
                'last_name': 'TestLastName',
                'zipcode': '10118',
                'phone_number': '+263771819478',
                'email': 'test_email@gmail.com',
                'password1': 'test_password',
                'password2': 'test_password',
            },
        }

        # lets get the number of users before saving another
        users_count = User.objects.count()

        # test to see if there are no messages in the outbox before we start saving the new user
        self.assertEqual(len(mail.outbox), 1)

        # test to see that all views will post correctly
        for url_name in self.keys:
            data_to_pass = dict(data[url_name])  # use dict to explicitly convert string to dictionary
            response = self.client.post(self.urls[url_name], data=data_to_pass)
            self.assertEqual(response.status_code, 302)

        # test to verify we have one more user
        self.assertEqual(User.objects.count(), users_count + 1)

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

        # test to see if there is now a new message in the outbox
        self.assertEqual(len(mail.outbox), 1)

        # Verify that the subject of the first message is correct.
        self.assertEqual(mail.outbox[0].subject, settings.ACTIVATION_EMAIL_SUBJECT)

        # test to see if a password reset object for the new user was created
        instances = PasswordReset.objects.filter(user=user)
        self.assertEqual(instances.count(), 1)

        # now lets see if we created an inactive user
        instance = instances[:1].get()
        user = instance.user
        self.assertEqual(user.is_active, False)

        # test to see if the activation link will work
        activation_url = reverse('register:activate-account', kwargs={'uuid': instance.uuid})
        self.assertEqual(self.client.get(activation_url).status_code, 200)
        self.assertTemplateUsed('register/activation-success.html')

        # now lets see if the user actually is active
        user = User.objects.get(id=user.id)
        self.assertEqual(user.is_active, True)

        # ok, so lets see that the PasswordReset Object was deleted
        instances = PasswordReset.objects.filter(user=user)
        self.assertEqual(instances.count(), 0)

        # now lets test with incorrect data to make sure all these give us 400 status codes,
        # these are the mandatory fields that cannot be skipped
        data = {
            'max_budget': {'budget': 'TEXT'},  # should be a number
            'personal_profile': {
                'first_name': 'TestFirstName',
                'last_name': 'TestLastName',
                'zipcode': '10118',
                'phone_number': '+263',
                'email': 'test_email@gmail.com',
                'password1': 'test_passwor',  # mismatching password
                'password2': 'test_password',
            },
        }

        # test to see that all views will post incorrectly
        for url_name in data:
            data_to_pass = dict(data[url_name])  # use dict to explicitly convert string to dictionary
            response = self.client.post(self.urls[url_name], data=data_to_pass)
            self.assertEqual(response.status_code, 400)

    def test_multi_registration(self):
        """
        We are doing this test to assert that multiple registrations can occur without mixing up the session variables
        """
        data = {
            'purchase_step': {'purchase_step': PS_DAP},
            'marital_status': {'status': SC_SI},
            'first_home': {'firsthome': True},
            'house_type': {'house_type': HT_SF, 'house_age': HA_15, 'house_cond': HC_SL},
            'city': {'preferred_city': ''},
            'max_budget': {'budget': 1200.59},
            'current_rent': {'current_rent': 321.49},
            'how_soon': {'how_soon': HS_3},
            'personal_profile': {
                'first_name': 'TestFirstName',
                'last_name': 'TestLastName',
                'zipcode': '10118',
                'phone_number': '+263771819478',
                'email': 'test_email@gmail.com',
                'password1': 'test_password',
                'password2': 'test_password',
            },
        }

        data_2 = {
            'purchase_step': {'purchase_step': PS_EAO},
            'marital_status': {'status': SC_INV},
            'first_home': {'firsthome': True},
            'house_type': {'house_type': HT_CN, 'house_age': HA_30, 'house_cond': HC_FU},
            'city': {'preferred_city': ''},
            'max_budget': {'budget': 564.11},
            'current_rent': {'current_rent': 76.67},
            'how_soon': {'how_soon': HS_12},
            'personal_profile': {
                'first_name': 'TestFirstName2',
                'last_name': 'TestLastName2',
                'zipcode': '10119',
                'phone_number': '+263771819479',
                'email': 'test_email2@gmail.com',
                'password1': 'test_password2',
                'password2': 'test_password2',
            },
        }

        # lets get the number of users before saving another
        users_count = User.objects.count()

        # test to see that all views will post correctly
        for url_name in self.keys:
            data_to_pass = dict(data[url_name])  # use dict to explicitly convert string to dictionary
            response = self.client.post(self.urls[url_name], data=data_to_pass)
            self.assertEqual(response.status_code, 302)

            data_to_pass_2 = dict(data_2[url_name])  # use dict to explicitly convert string to dictionary
            response = self.client_2.post(self.urls[url_name], data=data_to_pass_2)
            self.assertEqual(response.status_code, 302)

        # test to verify we have two more users
        self.assertEqual(User.objects.count(), users_count + 2)

        # test to ensure the users we just added got the session variables without mixing up
        user = User.objects.all().order_by('-id')[1:2].get()
        user_2 = User.objects.latest('id')

        # test to see that user got the correct information from the data dictionary
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

        # test to see that user_2 got the correct information from the data_2 dictionary
        self.assertEqual(user_2.purchase_step, data_2['purchase_step']['purchase_step'])
        self.assertEqual(user_2.status, data_2['marital_status']['status'])
        self.assertEqual(user_2.firsthome, data_2['first_home']['firsthome'])
        self.assertEqual(user_2.house_type, data_2['house_type']['house_type'])
        self.assertEqual(user_2.house_age, data_2['house_type']['house_age'])
        self.assertEqual(user_2.house_cond, data_2['house_type']['house_cond'])
        self.assertEqual(user_2.budget, data_2['max_budget']['budget'])
        self.assertEqual(user_2.current_rent, data_2['current_rent']['current_rent'])
        self.assertEqual(user_2.how_soon, data_2['how_soon']['how_soon'])

        self.assertEqual(user_2.email, data_2['personal_profile']['email'])
        self.assertEqual(user_2.zipcode, data_2['personal_profile']['zipcode'])
