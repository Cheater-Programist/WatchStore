from django.db import models

# Create your models here.
class Post(models.Model):
    image = models.ImageField(upload_to="posts/", verbose_name="Изображение")
    title = models.CharField(max_length=255, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'