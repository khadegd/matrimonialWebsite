from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext as _

class User(AbstractUser):
    email = models.EmailField(_('email address'), blank=False, unique=True)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,
            related_name='profile')
