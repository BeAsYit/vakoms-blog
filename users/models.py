from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager


class CustomUserManager(UserManager):
    pass


class CustomUser(AbstractUser):
    """
    Modify standard User model:
    Add new field 'phone'
    """
    phone = models.CharField(max_length=15, null=True)
    objects = CustomUserManager()