from django.contrib.auth.models import AbstractUser
from django.db import models

from mailing.models import NULLABLE


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='email')

    avatar = models.ImageField(upload_to='users/avatars', verbose_name='Аватар', **NULLABLE)
    phone = models.CharField(max_length=55, verbose_name='Телефон', **NULLABLE)
    country = models.CharField(max_length=100, verbose_name='Страна', **NULLABLE)


    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
