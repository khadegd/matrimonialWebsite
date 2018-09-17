from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext as _

from phonenumber_field.modelfields import PhoneNumberField

class User(AbstractUser):
    email = models.EmailField(_('email address'), blank=False, unique=True)
    contact = PhoneNumberField()

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,
            related_name='profile')
