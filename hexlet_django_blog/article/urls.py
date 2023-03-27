from django.urls import path
from hexlet_django_blog.article.views import CommentArticleView

urlpatterns = [
    path('', CommentArticleView.as_view(), name='comment_create'),
]
