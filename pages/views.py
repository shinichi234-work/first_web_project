from django.shortcuts import render
from .models import Article


def index(request):
    articles = Article.objects.all()
    context = {
        'title': 'RaceHub',
        'welcome_text': 'Your Ultimate Racing News Hub',
        'articles': articles,
    }
    return render(request, 'pages/index.html', context)


def about(request):
    return render(request, 'pages/about.html')
