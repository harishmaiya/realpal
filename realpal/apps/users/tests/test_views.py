from django.test import RequestFactory
from django.shortcuts import reverse
from test_plus.test import TestCase
from django.test import Client
from realpal.apps.users.constants import *
from realpal.apps.users.views import UserRedirectView, UserUpdateView
from realpal.apps.users.models import User


class BaseUserTestCase(TestCase):

    def setUp(self):
        self.user = self.make_user()
        self.factory = RequestFactory()


class TestUserRedirectView(BaseUserTestCase):

    client = Client()

    def test_get_redirect_url(self):
        # Instantiate the view directly. Never do this outside a test!
        view = UserRedirectView()
        # Generate a fake request
        request = self.factory.get('/fake-url')
        # Attach the user to the request
        request.user = self.user
        # Attach the request to the view
        view.request = request
        # Expect: '/users/testuser/', as that is the default username for
        #   self.make_user()
        self.assertEqual(
            view.get_redirect_url(),
            '/users/testuser/'
        )


class TestUserUpdateView(BaseUserTestCase):

    def setUp(self):
        # call BaseUserTestCase.setUp()
        super(TestUserUpdateView, self).setUp()
        # Instantiate the view directly. Never do this outside a test!
        self.view = UserUpdateView()
        # Generate a fake request
        request = self.factory.get('/fake-url')
        # Attach the user to the request
        request.user = self.user
        # Attach the request to the view
        self.view.request = request

    def test_get_success_url(self):
        # Expect: '/users/testuser/', as that is the default username for
        #   self.make_user()
        self.assertEqual(
            self.view.get_success_url(),
            '/users/~update/'
        )

    def test_get_object(self):
        # Expect: self.user, as that is the request's user object
        self.assertEqual(
            self.view.get_object(),
            self.user
        )

    def test_updating_user_info(self):
        update_url = reverse('users:update')
        data = {
            'purchase_step_form': {'purchase_step': PS_DAP},
            'marital_status_form': {'status': SC_SI},
            'first_home_form': {'firsthome': True},
            'house_type_form': {'house_type': HT_SF, 'house_age': HA_15, 'house_cond': HC_SL},
            'city_form': {'preferred_city': ''},
            'max_budget_form': {'budget': 1200.59},
            'current_rent_form': {'current_rent': 321.49},
            'how_soon_form': {'how_soon': HS_3},
            'personal_profile_form': {
                'first_name': 'TestFirstName',
                'last_name': 'TestLastName',
                'zipcode': '10118',
                'phone_number': '+263771819478',
                'email': 'test_email@gmail.com',
                'password1': 'test_password',
                'password2': 'test_password',
            },
        }

        for form in data:
            response = self.client.post(update_url, data[form].update({form: ''}))
            self.assertEqual(response.status_code, 302)

        user = self.view.get_object()
        self.assertEqual(user.purchase_step, data['purchase_step_form']['purchase_step'])
        self.assertEqual(user.status, data['marital_status_form']['status'])
        self.assertEqual(user.firsthome, data['first_home_form']['firsthome'])
        self.assertEqual(user.house_type, data['house_type_form']['house_type'])
        self.assertEqual(user.house_age, data['house_type_form']['house_age'])
        self.assertEqual(user.house_cond, data['house_type_form']['house_cond'])
        self.assertEqual(user.budget, data['max_budget_form']['budget'])
        self.assertEqual(user.current_rent, data['current_rent_form']['current_rent'])
        self.assertEqual(user.how_soon, data['how_soon_form']['how_soon'])

        self.assertEqual(user.email, data['personal_profile_form']['email'])
        self.assertEqual(user.zipcode, data['personal_profile_form']['zipcode'])
