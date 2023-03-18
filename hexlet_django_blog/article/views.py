from django.shortcuts import render

def index(request):
    return render(request, 'article_index.html', context={'title': 'Некоторая статья'})
