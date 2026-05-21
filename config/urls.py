from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from pages.views import index, about, article_detail, add_comment, article_create, article_update, contact, register

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('article/<int:pk>/', article_detail, name='article_detail'),
    path('article/<int:pk>/comment/', add_comment, name='add_comment'),
    path('article/new/', article_create, name='article_create'),
    path('article/<int:pk>/edit/', article_update, name='article_update'),
    path('contact/', contact, name='contact'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/register/', register, name='register'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
