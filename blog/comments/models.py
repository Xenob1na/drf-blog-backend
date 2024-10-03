from django.db import models
from django.contrib.auth.models import User
from blogapi.models import Post


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='Комментарии', on_delete=models.CASCADE)
    body = models.TextField(verbose_name='Текст', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создан')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Коммент_Создал', verbose_name='Создал', blank=True, null=True)

    def __str__(self):
        return self.body
