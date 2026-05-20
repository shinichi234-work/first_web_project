from django.contrib import admin
from django.urls import path, include
from pages.views import index, about, article_detail, article_create, article_update, contact, register

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('article/<int:pk>/', article_detail, name='article_detail'),
    path('article/new/', article_create, name='article_create'),
    path('article/<int:pk>/edit/', article_update, name='article_update'),
    path('contact/', contact, name='contact'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/register/', register, name='register'),
]
