from django.contrib.auth.models import AbstractUser
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _


@python_2_unicode_compatible
class User(AbstractUser):

    # First Name and Last Name do not cover name patterns
    # around the globe.
    name = models.CharField(_('Name of User'), blank=True, max_length=255)
    zipcode = models.CharField(max_length=10, blank=True, null=True)

    current_rent = models.FloatField(null=True)
    budget = models.FloatField(blank=True, null=True)
    annual_income = models.FloatField(blank=True, null=True)

    LANGUAGE_CHOICES = (
        ('EN', 'English'),
        ('ESP', 'Spanish'),
        ('CA', 'Mandarin/Cantonese'),
        ('HI', 'Hindi'),
        ('OT', 'Other'),
    )
    language = models.CharField(
        max_length=2, choices=LANGUAGE_CHOICES, default='EN'
    )

    STATUS_CHOICES = (
        ('SI', 'Single'),
        ('MNK', 'Married with No Kids'),
        ('MNSK', 'Married with No School Kids'),
        ('MSK', 'Married with School Kids'),
        ('INV', 'Investor')
    )
    status = models.CharField(
        max_length=4, choices=STATUS_CHOICES, default='SI'
    )

    HOUSE_TYPE_CHOICES = (
        ('SF', 'Single Family'),
        ('TH', 'Townhome'),
        ('CN', 'Condominium'),
        ('NC', 'New Construction'),
        ('OT', 'Other Options'),
        ('FX', 'Flexible')
    )
    house_type = models.CharField(
        max_length=2, choices=HOUSE_TYPE_CHOICES, blank=True
    )

    HOUSE_AGE_CHOICES = (
        ('NC', 'New Construction'),
        ('15', 'One to Fifteen'),
        ('30', 'Fifteen to thirty'),
        ('OLD', 'Over thirty')
    )
    house_age = models.CharField(
        max_length=3, choices=HOUSE_TYPE_CHOICES, blank=True
    )

    HOUSE_CONDITION_CHOICES = (
        ('UP', 'Updated'),
        ('SL', 'Slightly dated'),
        ('FU', 'Fixer Upper')
    )
    house_cond = models.CharField(
        max_length=3, choices=HOUSE_CONDITION_CHOICES, blank=True
    )

    CREDIT_SCORE_CHOICES = (
        ('780+', '780+'),
        ('740-779', '740-779'),
        ('700-739', '700-739'),
        ('650-699', '650-699'),
        ('600-649', '600-649'),
        ('<599', '<599')
    )
    credit_score = models.CharField(
        max_length=10, choices=CREDIT_SCORE_CHOICES, blank=True, null=True
    )


    firsthome = models.BooleanField(default=True)
    HOW_SOON_CHOICES = (
        ('3', '0-3 Months'),
        ('6', '3-6 Months'),
        ('12', '6-12 Months'),
        ('12+', '12+ Months'),
        ('SK', 'Skip')
    )

    how_soon = models.CharField(max_length=3, choices=HOW_SOON_CHOICES, null=True)


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
