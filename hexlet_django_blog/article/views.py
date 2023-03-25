from django.shortcuts import render, get_object_or_404
from django.views import View
from django.http import HttpResponse
from hexlet_django_blog.article.models import Article

#  Переделайте hexlet_django_blog.article.views.index в класс-потомок от View. 
#  В дальнейшем мы будем расширять этот класс
class ArticleIdView(View):
    template_name = "article/index.html"

    def get(self, request, *args, **kwargs):
        article = get_object_or_404(Article, id=kwargs['id'])
        return render(request, self.template_name, context={
            'article': article,
        })


class ArticleFirstView(View):
    template_name = "index.html"
    def get(self, request, *args, **kwargs):
        article = Article.objects.first()
        return render(request, self.template_name, context={
            'article': article,
        })

# Сделайте так, чтобы hexlet_django_blog.article.views.index принимала строковый параметр "tags" и 
# целочисленный параметр "article_id" из пути /article/tags/article_id и выводила текст в виде Статья номер 42. 
# Тег python
# def index(request, tags=None, article_id=None):
#     template_name = "article/index.html"
#     return render(request, template_name, context={'article_id': article_id, 'tags': tags})
