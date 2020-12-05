from django.db import models
from django.contrib.auth.models import User
from postsapp.models import Blog


class Subscription(models.Model):
    class Meta:
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'
    subscriber = models.ForeignKey(User, on_delete=models.CASCADE, related_name='subscription')
    source = models.ForeignKey(Blog, on_delete=models.CASCADE)
    is_active = models.BooleanField(verbose_name='активна', default=True)

# Create your models here.
