from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    confirm_password = models.CharField(max_length=50, verbose_name='Подтверждения пароля')

def __str__(self):
        return self.username
    
class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'