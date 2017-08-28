from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'realpal.apps.users'
    verbose_name = 'Users'

    def ready(self):
        """
        Initialize signals module, when the orders app is ready
        :return:
        """

        # Initialize signal module
        from .signals import signals

