from django.urls import path
from hexlet_django_blog.categories import views


urlpatterns = [
    path('', views.categories,name='app-views-categories'),
]
