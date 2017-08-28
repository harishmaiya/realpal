from django.test import RequestFactory
from django.shortcuts import reverse
from test_plus.test import TestCase
from django.test import Client
from realpal.apps.users.constants import *
from realpal.apps.users.views import UserRedirectView, UserUpdateView


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
            '/users/~update/#success'
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
            },
        }

        # let's login first since this view is only reachable after login
        self.client.login(username='testuser', password='password')

        # test to see if we reached the user update profile page
        self.assertTemplateUsed('users/update.html')

        for form in data:
            data_to_pass = data[form]
            data[form][form] = 'Update'
            response = self.client.post(update_url, data_to_pass)
            self.assertEqual(response.status_code, 302)
            self.assertTemplateUsed('users/update.html')

        # test to see that trying to update with incorrect data will return us to
        # update page without the success redirect
        incorrect_data = {
            'purchase_step_form': {'purchase_step': 8},  # 8 is not a valid option
            'marital_status_form': {'status': 8},
            'house_type_form': {'house_type': 8, 'house_age': 8, 'house_cond': 8},
            'max_budget_form': {'budget': 'TEXT'},
            'current_rent_form': {'current_rent': 'TEXT'},  # TEXT is not a valid number
            'how_soon_form': {'how_soon': 8},
            'personal_profile_form': {
                'first_name': 'TestFirstName',
                'last_name': 'TestLastName',
                'zipcode': '10118',
                'phone_number': '+26334465657456774567',  # number too long
                'email': 'test_email@gmail.com',
            },
        }

        for form in incorrect_data:
            data_to_pass = incorrect_data[form]
            incorrect_data[form][form] = 'Update'
            response = self.client.post(update_url, data_to_pass)
            self.assertEqual(response.status_code, 200)
            self.assertTemplateUsed('users/update.html')

