import logging

from django.db.models.signals import post_save
from django.dispatch import receiver

from realpal.apps.chat.models import Room
from realpal.users.models import User

logger = logging.getLogger(__name__)


@receiver(post_save, sender=User)
def user_post_save_callback(sender, **kwargs):
    """
    Called every time a User is created or updated
    :param sender: The model that sent the signal to this method
    :param kwargs: Information about the instance that sent the signal e.g. instance = kwargs['instance']
    :return:
    """

    if kwargs.get('created', False):
        user = kwargs.get('instance')
        user_new_room, created = Room.objects.get_or_create(
            client=user
        )
        if created:
            logger.debug('{} created'.format(user_new_room))
