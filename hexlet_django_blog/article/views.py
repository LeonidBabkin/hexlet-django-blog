from django.shortcuts import render

def index(request):
    return render(request, 'hexlet-django-blog/hexlet_django_blog/article/templates/index.html', context={'title': 'Некоторая статья'})
