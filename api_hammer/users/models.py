from django.db import models

from .invite_code import get_invite_code


class User(models.Model):
    phone = models.TextField(unique=True, max_length=50)
    password = models.TextField(unique=True, max_length=50)
    invite_code = models.TextField(default=get_invite_code())
    activation = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
    
    def __str__(self):
        return self.phone
