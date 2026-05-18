from django.shortcuts import render, get_object_or_404, redirect
from .models import Article
from .forms import FeedbackForm


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


def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    context = {'article': article}
    return render(request, 'pages/article_detail.html', context)


def contact(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            return redirect('home')
    else:
        form = FeedbackForm()
    return render(request, 'pages/contact.html', {'form': form})
