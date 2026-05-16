from django.contrib import admin
from django.urls import path
from pages.views import index, about, article_detail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('article/<int:pk>/', article_detail, name='article_detail'),
]
