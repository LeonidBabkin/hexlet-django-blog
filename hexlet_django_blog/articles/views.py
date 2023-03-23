from django.shortcuts import render
from django.http import Http404
from django.views.decorators.http import require_http_methods


articles_list = [
    {'id': 1, 'title': '"How to foo?"', 'author': 'F. BarBaz'},
    {'id': 2, 'title': '"Force 101"', 'author': 'O-W. Kenobi'},
    {'id': 3, 'title': '"Top 10 skyscrapers"', 'author': 'K. Kong'},
    {'id': 4, 'title': '"Top 10 skyscrapers (jp. edition)"', 'author': 'K. Godzilla'},
    {'id': 5, 'title': '"5 min recepies"', 'author': 'H. Lector'},
]
# Create your views here.
def articles(request):
    return render(request, 'articles.html')


@require_http_methods(['GET'])
def article_id(request, id):
    for article in articles_list:
        if article['id'] == id:
            return render(request, 'articles.html', context={'article': article})
    raise Http404()



