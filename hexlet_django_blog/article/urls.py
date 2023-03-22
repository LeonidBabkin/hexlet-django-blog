from django.urls import path
# from hexlet_django_blog.article.views import ArticleIndexView
from hexlet_django_blog.article import views

urlpatterns = [
    path('article/<str:tags>/<int:article_id>', views.index, name='article')
#     path('', ArticleIndexView.as_view(), name='article-index-view'),
    
]
