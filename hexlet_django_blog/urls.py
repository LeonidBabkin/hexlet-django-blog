"""hexlet_django_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from hexlet_django_blog import views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', views.index),  # <правило,назначает обработчиком главной страницы или пустого пути вьюху views.index.
    path('about/', views.about),
    path('details/', views.details),
    path('article/', include('hexlet_django_blog.article.urls')),  # <- новая строчка
    path('articles/', include('hexlet_django_blog.articles.urls')),
    path('categories/', include('hexlet_django_blog.categories.urls')),
    path('admin/', admin.site.urls),
]
