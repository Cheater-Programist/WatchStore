from django.db import models
from datetime import date
from django.contrib.auth import get_user_model
from django.core.validators import RegexValidator 
from django.contrib.auth.models import AbstractUser

phone_regex = RegexValidator(regex=r'^\+996\d{9}$', message="Номер телефона необходимо ввести в формате: '+996xxxxxxxxx'.")

# Create your models here.
class User(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True)
    phone = models.CharField(validators=[phone_regex], max_length=15, verbose_name='Номер телефона')
    confirm_password = models.CharField(max_length=50, verbose_name='Подтверждения пароля')
    user_age = models.IntegerField(verbose_name="Возраст", null=True, blank=True)

    def __str__(self):
        return self.username

    @property
    def age(self):
        if self.date_of_birth:
            today = date.today()
            age = today.year - self.date_of_birth.year
            if today.month < self.date_of_birth.month or (today.month == self.date_of_birth.month and today.day < self.date_of_birth.day):
                age -= 1
                self.user_age = age
                self.save()
                return age
            return None
    
    class Meta:
            verbose_name = 'Пользователь'
            verbose_name_plural = 'Пользователи'