from django.urls import path
from hexlet_django_blog.article.views import ArticleIdView, ArticleFirstView
from hexlet_django_blog.article import views


urlpatterns = [
#  Назначьте hexlet_django_blog.article.views.index имя "article"
#     path('<str:tags>/<int:article_id>', views.index, name='article')
    path('<int:id>', ArticleIdView.as_view()),
    path('', ArticleFirstView.as_view(), name='article-index-view'),
]
