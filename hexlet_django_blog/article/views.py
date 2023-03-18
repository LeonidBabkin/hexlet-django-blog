from django.shortcuts import render

def index(request):
    return render(request, 'article/templates/index.html', context={'title': 'Некоторая статья'})
