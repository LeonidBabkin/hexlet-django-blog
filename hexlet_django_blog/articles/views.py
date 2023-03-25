from django.shortcuts import render, redirect
from django.http import Http404
from django.views.decorators.http import require_http_methods
from hexlet_django_blog.article.models import Article
from django.views import View

articles_list = [
    {'id': 1, 'title': '"How to foo?"', 'author': 'F. BarBaz'},
    {'id': 2, 'title': '"Force 101"', 'author': 'O-W. Kenobi'},
    {'id': 3, 'title': '"Top 10 skyscrapers"', 'author': 'K. Kong'},
    {'id': 4, 'title': '"Top 10 skyscrapers (jp. edition)"', 'author': 'K. Godzilla'},
    {'id': 5, 'title': '"5 min recepies"', 'author': 'H. Lector'},
]
# Create your views here.


#  Переделайте hexlet_django_blog.article.views.index в класс-потомок от View. 
#  В дальнейшем мы будем расширять этот класс
class IndexView(View):
    template_name = 'articles/index.html'

    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()[:15]  # Первой строкой из базы извлекаются 15 первых статей. Django автоматически определяет наличие размера списка в запросе и выполняет правильное смещение в SQL.
        return render(request, self.template_name, context={
            'articles': articles,
        })



@require_http_methods(['GET'])
def article_id(request, id):
    for article in articles_list:
        if article['id'] == id:
            return render(request, 'articles.html', context={'article': article})
    raise Http404()
