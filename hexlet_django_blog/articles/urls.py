from django.urls import path
from hexlet_django_blog.articles import views


urlpatterns = [
    path('', views.IndexView.as_view(), name='articles_index'),
    path('<int:id>', views.ArticleView.as_view(), name='articles_detail'),
    path('create/', views.ArticleFormCreateView.as_view(), name='articles_create'),
]
