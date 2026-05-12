from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=200, verbose_name='Title')
    content = models.TextField(verbose_name='Content')
    views_count = models.IntegerField(default=0, verbose_name='Views')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Published')

    def __str__(self):
        return self.title
