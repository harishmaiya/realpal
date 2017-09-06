from django.conf import settings
from django.core import mail
from django.test import Client, TestCase
from django.urls import reverse
from realpal.apps.users.constants import *
from realpal.apps.users.models import User, PasswordReset


class RegistrationTest(TestCase):
    client = Client()
    client_2 = Client()

    # here we create this list of keys so we can iterate in this order, the personal profile step must be the last
    keys = ('purchase_step', 'marital_status', 'first_home', 'house_type', 'city', 'max_budget', 'current_rent',
            'how_soon', 'personal_profile')

    urls = {
        'purchase_step': reverse('onboarding:purchase-step'),
        'marital_status': reverse('onboarding:marital-status'),
        'first_home': reverse('onboarding:first-home'),
        'house_type': reverse('onboarding:house-type'),
        'city': reverse('onboarding:city'),
        'max_budget': reverse('onboarding:max-budget'),
        'current_rent': reverse('onboarding:current-rent'),
        'how_soon': reverse('onboarding:how-soon'),
        'personal_profile': reverse('onboarding:personal-profile'),
    }

    def test_get(self):
        # test to see that all pages are reachable when user is not logged in
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
        self.assertEqual(len(mail.outbox), 0)

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
        self.assertEqual(mail.outbox[0].subject, settings.EMAIL_SUBJECT_PREFIX)

        # test to see if a password reset object for the new user was created
        instances = PasswordReset.objects.filter(user=user)
        self.assertEqual(instances.count(), 1)

        # now lets see if we created an inactive user
        instance = instances[:1].get()
        user = instance.user
        self.assertEqual(user.is_active, False)

        # test to see if the activation link will work
        activation_url = reverse('onboarding:activate-account', kwargs={'uuid': instance.uuid})
        self.assertEqual(self.client.get(activation_url).status_code, 200)
        self.assertTemplateUsed('register/activation_success.html')

        # now lets see if the user actually is active
        user = User.objects.get(id=user.id)
        self.assertEqual(user.is_active, True)

        # ok, so lets see that the PasswordReset Object was deleted
        instances = PasswordReset.objects.filter(user=user)
        self.assertEqual(instances.count(), 0)

        # now lets logging and test that the onboarding urls redirect to chat
        self.client.login(email='test_email@gmail.com', password='test_password')
        for url_name in self.keys:
            response = self.client.get(self.urls[url_name])
            self.assertEqual(response.status_code, 302)
            self.assertTemplateUsed('chat/client.html')

    def test_wrong_post(self):
        # now lets test with incorrect data to make sure all these give us 400 status codes,
        # these are the mandatory fields that cannot be skipped
        wrong_data = {
            'max_budget': {'budget': 'TEXT'},  # should be a number
            'current_rent': {'current_rent': 'TEXT'},  # should be a number
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
        for url_name in wrong_data:
            data_to_pass = wrong_data[url_name]  # use dict to explicitly convert string to dictionary
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
            'house_type': {'house_type': HT_CN, 'house_age': HA_OLD, 'house_cond': HC_FU},
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

    def test_skipping_fields(self):

        # test to make sure skipping purchase step is not allowed
        data = {'purchase_step': None}
        response = self.client.post(self.urls['purchase_step'], data=data)
        self.assertEqual(response.status_code, 400)
        # lets see if we are returned to the same template
        self.assertTemplateUsed('onboarding/purchase_step.html')

        # test to make sure that we can supply a correct value for purchase step
        data = {'purchase_step': PS_EAO}
        response = self.client.post(self.urls['purchase_step'], data=data)
        self.assertEqual(response.status_code, 302)
        # lets see if we are taken to the next template marital status
        self.assertTemplateUsed('onboarding/marital_status.html')

        # test to make sure we can skip marital status
        data = {'marital_status': None}
        response = self.client.post(self.urls['marital_status'], data=data)
        self.assertEqual(response.status_code, 302)
        # lets see if we are taken to the next template first home
        self.assertTemplateUsed('onboarding/first_home.html')

        # test to make sure we are unable to skip first home stage
        data = {'firsthome': ''}
        response = self.client.post(self.urls['first_home'], data=data)
        self.assertEqual(response.status_code, 400)
        # lets see if we remain on the same template
        self.assertTemplateUsed('onboarding/first_home.html')

        # test to make sure that we can supply a correct value for first home
        data = {'firsthome': False}
        response = self.client.post(self.urls['first_home'], data=data)
        self.assertEqual(response.status_code, 302)
        # lets see if we are taken to the next template house choices
        self.assertTemplateUsed('onboarding/marital_status.html')

        # test to make sure we can skip the house type form
        data = {'house_type': '', 'house_age': '', 'house_cond': ''}
        response = self.client.post(self.urls['house_type'], data=data)
        self.assertEqual(response.status_code, 302)
        # lets see if we are taken to the next template city
        self.assertTemplateUsed('onboarding/city.html')

        # test to make sure we can skip the city form by choosing the `anywhere in silicon valley` option
        data = {'preferred_city': None}
        response = self.client.post(self.urls['city'], data=data)
        self.assertEqual(response.status_code, 302)
        # lets see if we are taken to the next template city
        self.assertTemplateUsed('onboarding/max_budget.html')

        # test to make sure we can skip the max budget form
        data = {'budget': ''}
        response = self.client.post(self.urls['max_budget'], data=data)
        self.assertEqual(response.status_code, 302)
        # lets see if we are taken to the next template current rent
        self.assertTemplateUsed('onboarding/current_rent.html')

        # test to make sure we can skip the current rent form
        data = {'current_rent': ''}
        response = self.client.post(self.urls['current_rent'], data=data)
        self.assertEqual(response.status_code, 302)
        # lets see if we are taken to the next template how soon
        self.assertTemplateUsed('onboarding/how_soon.html')

        # test to make sure we can skip the how soon form
        data = {'how_soon': ''}
        response = self.client.post(self.urls['how_soon'], data=data)
        self.assertEqual(response.status_code, 302)
        # lets see if we are taken to the next template personal profile
        self.assertTemplateUsed('onboarding/personal_profile.html')

        # test to make sure we are unable to skip the personal profile form without a valid form
        data = {
            'first_name': 'TestFirstName',
            'last_name': 'TestLastName',
            'zipcode': '10119',
            'phone_number': '+263771819478',
            'email': 'test_email2@gmail.com',
            'password1': 'test_password',
            'password2': 'test_password',
        }
        response = self.client.post(self.urls['personal_profile'], data=data)
        self.assertEqual(response.status_code, 302)
        # lets see if we remain on the same template
        self.assertTemplateUsed('onboarding/personal_profile.html')

        user = User.objects.latest('id')
        self.assertEqual(user.purchase_step, PS_EAO)
        self.assertEqual(user.status, None)
        self.assertEqual(user.firsthome, False)
        self.assertEqual(user.house_type, None)
        self.assertEqual(user.house_age, None)
        self.assertEqual(user.house_cond, None)
        self.assertEqual(user.budget, None)
        self.assertEqual(user.current_rent, None)
        self.assertEqual(user.how_soon, None)

        self.assertEqual(user.email, 'test_email2@gmail.com')
        self.assertEqual(user.zipcode, '10119')






