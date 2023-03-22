from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse


#  Переделайте hexlet_django_blog.article.views.index в класс-потомок от View. В дальнейшем мы будем расширять этот класс
# class ArticleIndexView(View):
#     template_name = "article/index.html"

#     def get(self, request, *args, **kwargs):
#         return render(request, self.template_name, context={'title': 'Некоторая статья'})


def index(request, tags: str, article_id: int):
    template_name = "article/index.html"
    reversed_url = reverse('article', args=(article_id, tags))
    return render (reversed_url, template_name, context={'article_id': article_id, 'tags': tags})
