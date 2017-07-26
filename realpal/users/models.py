from django.contrib.auth.models import AbstractUser
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _


class City(models.Model):
    name = models.CharField(max_length=60)
    state = models.CharField(max_length=40)


@python_2_unicode_compatible
class User(AbstractUser):
    LANGUAGE_CHOICES = (
        ('EN', 'English'),
        ('ESP', 'Spanish'),
        ('CA', 'Mandarin/Cantonese'),
        ('HI', 'Hindi'),
        ('OT', 'Other'),
    )
    # First Name and Last Name do not cover name patterns
    # around the globe.
    name = models.CharField(_('Name of User'), blank=True, max_length=255)
    language = models.CharField(
        max_length=2, choices=LANGUAGE_CHOICES, default='EN'
    )

    STATUS_CHOICES = (
        ('SI', 'Single'),
        ('MNK', 'Married with No Kids'),
        ('MNSK', 'Married with No School Kids'),
        ('MSK', 'Married with School Kids'),
    )
    status = models.CharField(
        max_length=4, choices=STATUS_CHOICES, default='SI'
    )
    current_rent = models.FloatField(null=True)

    HOME_TYPE_CHOICES = (
        ('SF', 'Single Family'),
        ('TH', 'Townhome'),
        ('CN', 'Condominium'),
        ('OT', 'Other Options')
    )
    zipcode = models.CharField(max_length=10, blank=True, null=True)
    home_type = models.CharField(
        max_length=2, choices=HOME_TYPE_CHOICES, blank=True
    )
    budget = models.FloatField(blank=True, null=True)
    annual_income = models.FloatField(blank=True, null=True)

    CREDIT_SCORE_CHOICES = (
        ('780+', '780+'),
        ('740-779', '740-779'),
        ('700-739', '700-739'),
        ('660-699', '600-699'),
        ('600-659', '600-659'),
        ('<599', '<599')
    )
    credit_score = models.CharField(
        max_length=10, choices=CREDIT_SCORE_CHOICES, blank=True, null=True
    )
    interested_cities = models.ForeignKey(
        City, related_name='interested_users', null=True
    )

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('users:detail', kwargs={'username': self.username})
