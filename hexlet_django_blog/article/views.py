from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from hexlet_django_blog.article.models import Article

#  Переделайте hexlet_django_blog.article.views.index в класс-потомок от View. 
#  В дальнейшем мы будем расширять этот класс
class ArticleIndexView(View):
    template_name = "article/index.html"

    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()[:15]  # Первой строкой из базы извлекаются 15 первых статей. Django автоматически определяет наличие размера списка в запросе и выполняет правильное смещение в SQL.
        return render(request, self.template_name, context={
            'articles': articles,
        })


# Сделайте так, чтобы hexlet_django_blog.article.views.index принимала строковый параметр "tags" и 
# целочисленный параметр "article_id" из пути /article/tags/article_id и выводила текст в виде Статья номер 42. 
# Тег python
# def index(request, tags=None, article_id=None):
#     template_name = "article/index.html"
#     return render(request, template_name, context={'article_id': article_id, 'tags': tags})
