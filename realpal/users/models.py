from django.contrib.auth.models import AbstractUser
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from django.core.validators import RegexValidator
from realpal.users.constants import *


@python_2_unicode_compatible
class User(AbstractUser):

    # First Name and Last Name do not cover name patterns
    # around the globe.

    user_type = models.SmallIntegerField(choices=USER_TYPE_CHOICES, default=CLIENT_USER)
    name = models.CharField(_('Name of User'), blank=True, max_length=255)
    zipcode = models.CharField(max_length=10, blank=True, null=True)

    phone_regex = RegexValidator(
        regex=r'^\+?\d{9,15}$',
        message="Phone number must be entered in the format: '+2777181947'. Up to 15 digits allowed."
    )
    phone_number = models.CharField(validators=[phone_regex], blank=True, max_length=16)

    annual_income = models.FloatField(blank=True, null=True)

    purchase_step = models.SmallIntegerField(
        max_length=3, choices=PURCHASE_STEP_CHOICES, default='DAP'
    )

    status = models.SmallIntegerField(
        max_length=4, choices=STATUS_CHOICES, default=SC_SI
    )

    firsthome = models.BooleanField(default=True)

    house_type = models.SmallIntegerField(
        max_length=2, choices=HOUSE_TYPE_CHOICES, blank=True
    )

    house_age = models.SmallIntegerField(
        max_length=3, choices=HOUSE_AGE_CHOICES, blank=True
    )

    house_cond = models.SmallIntegerField(
        max_length=3, choices=HOUSE_CONDITION_CHOICES, blank=True
    )

    budget = models.FloatField(blank=True, null=True)
    current_rent = models.FloatField(blank=True, null=True)

    how_soon = models.SmallIntegerField(max_length=3, choices=HOW_SOON_CHOICES, null=True)

    language = models.SmallIntegerField(
        max_length=2, choices=LANGUAGE_CHOICES, default=LC_EN
    )

    credit_score = models.SmallIntegerField(
        max_length=10, choices=CREDIT_SCORE_CHOICES, blank=True, null=True
    )

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('users:detail', kwargs={'username': self.username})


class City(models.Model):
    name = models.CharField(max_length=60)
    state = models.CharField(max_length=40)
    interested_users = models.ForeignKey(
        User, related_name='cities', null=True
    )
