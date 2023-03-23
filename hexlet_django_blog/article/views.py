from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
# from django.urls import reverse


#  Переделайте hexlet_django_blog.article.views.index в класс-потомок от View. В дальнейшем мы будем расширять этот класс
# class ArticleIndexView(View):
#     template_name = "article/index.html"

#     def get(self, request, *args, **kwargs):
#         return render(request, self.template_name, context={'title': 'Некоторая статья'})


def index(request, tags=None, article_id=None):
    template_name = "article/index.html"
#     reversed_url = reverse('article', kwargs=('article_id'=42, 'tags'='python'))
    return render(request, template_name, context={'article_id': article_id, 'tags': tags})
