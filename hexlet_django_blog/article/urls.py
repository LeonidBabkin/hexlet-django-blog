from django.urls import path
from hexlet_django_blog.article.views import CommentFormView

urlpatterns = [
    path('', CommentFormView.as_view(), name='comment_create'),
]
