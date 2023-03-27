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
from django.urls import include, path
from hexlet_django_blog import views
from django.contrib import admin


urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('article/', include('hexlet_django_blog.article.urls')),
    path('articles/', include('hexlet_django_blog.articles.urls')),
    path('categories/', include('hexlet_django_blog.categories.urls')),
    path('admin/', admin.site.urls),
]
