from django.db import models
from django.contrib.auth.models import User


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Tag')

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=200, verbose_name='Title')
    content = models.TextField(verbose_name='Content')
    views_count = models.IntegerField(default=0, verbose_name='Views')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Published')
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Author')
    image = models.ImageField(upload_to='articles/', blank=True, null=True, verbose_name='Image')
    tags = models.ManyToManyField(Tag, blank=True, related_name='articles', verbose_name='Tags')

    def __str__(self):
        return self.title


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments', verbose_name='Article')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Author')
    text = models.TextField(verbose_name='Comment')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.author} — {self.article}'
