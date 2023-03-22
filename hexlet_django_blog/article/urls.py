from django.urls import path
# from hexlet_django_blog.article.views import ArticleIndexView
from hexlet_django_blog.article import views

urlpatterns = [
    path('<str: tags>/<int: article_id>', views.index)
#     path('', ArticleIndexView.as_view(), name='article-index-view'),
    
]
