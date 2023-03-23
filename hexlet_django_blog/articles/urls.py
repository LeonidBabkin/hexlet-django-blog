from django.urls import path
from hexlet_django_blog.articles import views


urlpatterns = [
    path('', views.articles, name='app-views-articles'),
    path('<int:id>/', views.article_id, name='article_id'),
]
