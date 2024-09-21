from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок', blank=True, null=True)
    body = models.TextField(verbose_name='Текст', blank=True, null=True)
    description = models.TextField(verbose_name='Описание', blank=True, null=True)
    image = models.ImageField(upload_to='images/', verbose_name='Изображение', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создан')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлен')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Создал', verbose_name='Создал', blank=True, null=True)

    def __str__(self):
        return self.title
