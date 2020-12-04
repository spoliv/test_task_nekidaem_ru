from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post_title = models.CharField(verbose_name='заголовок поста', max_length=50)
    post_body = models.TextField(verbose_name='текст поста', blank=True)
    date_created = models.DateTimeField(verbose_name='создан', auto_now_add=True)
# Create your models here.
