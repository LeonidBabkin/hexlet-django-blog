from django.urls import path
from hexlet_django_blog.articles import views


urlpatterns = [
    path('hexlet-django-blog/articles', views.articles),
]
