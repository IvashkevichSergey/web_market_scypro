from random import randint

from django.contrib.auth.models import AbstractUser
from django.db import models

from catalog.models import NULLABLE


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='email')

    phone = models.CharField(**NULLABLE, max_length=15, verbose_name='телефон')
    country = models.CharField(**NULLABLE, max_length=15, verbose_name='страна')
    avatar = models.ImageField(**NULLABLE, upload_to='users/', verbose_name='аватар')
    is_active = models.BooleanField(default=False, verbose_name='статус верификации')
    verification_code = models.CharField(max_length=10, default=''.join(str(randint(0, 10)) for _ in range(6)))

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
