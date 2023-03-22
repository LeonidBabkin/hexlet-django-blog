from django.shortcuts import render
from django.views import View

#  Переделайте hexlet_django_blog.article.views.index в класс-потомок от View. В дальнейшем мы будем расширять этот класс
# class ArticleIndexView(View):
#     template_name = "article/index.html"

#     def get(self, request, *args, **kwargs):
#         return render(request, self.template_name, context={'title': 'Некоторая статья'})
def index(request):
    template_name = "article/index.html"
    return render(request, template_name, 
