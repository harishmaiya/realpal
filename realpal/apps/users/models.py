import uuid
import logging

from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.core.mail import EmailMultiAlternatives
from django.core.urlresolvers import reverse
from django.core.validators import RegexValidator
from django.db import models
from django.template import loader
from django.utils.encoding import python_2_unicode_compatible
from django.utils.html import strip_tags
from django.utils.translation import ugettext_lazy as _
from .managers import UserManager
from realpal.apps.users.constants import *

logger = logging.getLogger(__name__)


@python_2_unicode_compatible
class City(models.Model):
    name = models.CharField(max_length=60)
    state = models.CharField(max_length=40)

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class User(AbstractUser):
    first_name = models.CharField(_('first name'), max_length=255)
    last_name = models.CharField(_('last name'), max_length=255)
    email = models.EmailField(unique=True, null=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()

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

    status = models.SmallIntegerField(choices=STATUS_CHOICES, blank=True, null=True)

    firsthome = models.BooleanField(default=False)

    has_mortgage = models.BooleanField(default=False)

    has_agent = models.BooleanField(default=False)

    house_type = models.SmallIntegerField(choices=HOUSE_TYPE_CHOICES, blank=True, null=True)

    house_age = models.SmallIntegerField(choices=HOUSE_AGE_CHOICES,  blank=True, null=True)

    house_cond = models.SmallIntegerField(choices=HOUSE_CONDITION_CHOICES, blank=True, null=True)

    preferred_city = models.ManyToManyField(City)

    budget = models.FloatField(blank=True, null=True)

    current_rent = models.FloatField(blank=True, null=True)

    how_soon = models.SmallIntegerField(choices=HOW_SOON_CHOICES, null=True, blank=True)

    language = models.SmallIntegerField(choices=LANGUAGE_CHOICES, default=LC_EN)

    credit_score = models.SmallIntegerField(choices=CREDIT_SCORE_CHOICES, null=True)

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('users:detail', kwargs={'username': self.username})

    @property
    def full_name(self):
        return self.get_full_name()

    def get_full_name(self):
        """
        Return first name and last name combined as the full name
        """
        full_name = "%s %s" % (self.first_name, self.last_name)
        if not len(full_name.strip()):
            full_name = self.username
        return full_name

    def get_short_name(self):
        return self.email

    def send_confirmation_email(self):
        token = PasswordReset.objects.create(user=self)
        link = '{}{}'.format(settings.BASE_URL, reverse('onboarding:activate-account', kwargs={'uuid': token.uuid}))

        context = {
            'activation_link': link,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'subject': settings.EMAIL_SUBJECT_PREFIX,
        }

        template = 'onboarding/activation_email.html'

        msg = EmailMultiAlternatives(
            subject=settings.EMAIL_SUBJECT_PREFIX,
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=[self.email],
            headers={"Reply-To:": settings.DEFAULT_FROM_EMAIL}
        )
        self.send_email(context, msg, template)

    def send_welcome_email(self):

        context = {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'subject': settings.EMAIL_SUBJECT_PREFIX,
        }
        template = 'onboarding/welcome_email.html'

        msg = EmailMultiAlternatives(
            subject=settings.EMAIL_SUBJECT_PREFIX,
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=[self.email],
            headers={"Reply-To:": settings.DEFAULT_FROM_EMAIL}
        )
        self.send_email(context, msg, template)

    def send_email(self, context, msg, template):
        email_html = loader.get_template(template).render(context)
        email_txt = strip_tags(email_html)
        msg.body = email_txt
        msg.attach_alternative(email_html, 'text/html')
        try:
            msg.send(fail_silently=False)
        except Exception as er:
            logger.error('failed sending email for {}'.format(self.get_full_name()))


class PasswordReset(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    uuid = models.CharField(max_length=64, verbose_name=u"Activation key", default=uuid.uuid1)
    date_created = models.DateField(auto_now_add=True)
