from django.contrib.auth.models import AbstractUser
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from django.core.validators import RegexValidator
from realpal.users.constants import *
import uuid


class City(models.Model):
    name = models.CharField(max_length=60)
    state = models.CharField(max_length=40)


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

    purchase_step = models.SmallIntegerField(choices=PURCHASE_STEP_CHOICES, default=PS_DAP)

    status = models.SmallIntegerField(choices=STATUS_CHOICES, default=SC_SI)

    firsthome = models.BooleanField(default=True)

    house_type = models.SmallIntegerField(choices=HOUSE_TYPE_CHOICES, null=True)

    house_age = models.SmallIntegerField(choices=HOUSE_AGE_CHOICES, null=True)

    house_cond = models.SmallIntegerField(choices=HOUSE_CONDITION_CHOICES, null=True)

    preferred_city = models.ForeignKey(City, blank=True, null=True)

    budget = models.FloatField(blank=True, null=True)

    current_rent = models.FloatField(blank=True, null=True)

    how_soon = models.SmallIntegerField(choices=HOW_SOON_CHOICES, null=True)

    language = models.SmallIntegerField(choices=LANGUAGE_CHOICES, default=LC_EN)

    credit_score = models.SmallIntegerField(choices=CREDIT_SCORE_CHOICES, null=True)

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('users:detail', kwargs={'username': self.username})


class PasswordReset(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    uuid = models.CharField(max_length=64, verbose_name=u"Activation key", default=uuid.uuid1)
    date_created = models.DateField(auto_now_add=True)
