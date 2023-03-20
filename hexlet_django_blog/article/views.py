from django.shortcuts import render
from django.views import View


class ArticleIndexView(View):
    template_name = "article/index.html"

    def get(self, request, *args, **kwargs):
        return render(request, context={'title': 'Некоторая статья'})
