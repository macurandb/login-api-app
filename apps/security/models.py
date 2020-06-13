from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, AbstractUser
from .managers import CustomUserManager
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    username = None
    first_name = models.CharField(_('First Name'), max_length=30)
    last_name = models.CharField(_('Last Name'), max_length=30)
    email = models.EmailField(unique=True)
    age = models.IntegerField()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'age', 'password']

    objects = CustomUserManager()

