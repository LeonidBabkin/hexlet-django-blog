from django.shortcuts import get_object_or_404, render
from django.views import View
from hexlet_django_blog.articles.models import Article
from django.db.models import Q


# class IndexView(View):
#     template_name = 'articles/index.html'
#
#     def get(self, request, *args, **kwargs):
#         articles = Article.objects.all()
#         return render(request, self.template_name, context={
#             'articles': articles,
#         })
class IndexView(View):
    # BEGIN (write your solution here)
    def get(self, request, *args, **kwargs):
        query = request.GET.get('q', '')
        articles = Article.objects.filter(Q(title__icontains=query))
        return render(request, 'articles/index.html', context={
            'articles': articles,
            'query': query,
        })


class ArticleView(View):
    template_name = 'articles/article.html'

    def get(self, request, *args, **kwargs):
        article = get_object_or_404(Article, id=kwargs['id'])
        return render(request, self.template_name, context={
            'article': article,
        })
