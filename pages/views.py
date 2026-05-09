from django.shortcuts import render


def index(request):
    context = {
        'title': 'RaceHub',
        'welcome_text': 'Your Ultimate Racing News Hub',
    }
    return render(request, 'pages/index.html', context)


def about(request):
    return render(request, 'pages/about.html')
