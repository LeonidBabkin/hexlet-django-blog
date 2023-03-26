from django.shortcuts import get_object_or_404, render
from django.views import View
from hexlet-django-blog.articles.models import Article


class IndexView(View):
    template_name = 'articles/index.html'

    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()
        return render(request, self.template_name, context={
            'articles': articles,
        })


class ArticleView(View):
    template_name = 'articles/article.html'

    def get(self, request, *args, **kwargs):
        article = get_object_or_404(Article, id=kwargs['id'])
        return render(request, self.template_name, context={
            'article': article,
        })

    raise Http404()
