from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
User = get_user_model()

class Post(models.Model):
    image = models.ImageField(upload_to="posts/", verbose_name="Изображение")
    title = models.CharField(max_length=255, verbose_name="Название")
    price = models.PositiveIntegerField(verbose_name="Цена")
    description = models.TextField(verbose_name="Описание")

    def __str__(self) -> str:
        return f"{self.title} || {self.price}"
    
    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'