from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext as _

from phonenumber_field.modelfields import PhoneNumberField

class User(AbstractUser):
    email = models.EmailField(_('email address'), blank=False, unique=True,
            help_text='Required.')
    contact = PhoneNumberField(_('contact number'), blank=False, unique=True,
            help_text=('Required. Use +country_code-contact. '
            'e.g. +91-7218000000'))

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,
            related_name='profile')
