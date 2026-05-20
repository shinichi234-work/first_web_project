from django.db import models
from django.contrib.auth.models import User


class Article(models.Model):
    title = models.CharField(max_length=200, verbose_name='Title')
    content = models.TextField(verbose_name='Content')
    views_count = models.IntegerField(default=0, verbose_name='Views')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Published')

    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Author')

    def __str__(self):
        return self.title
