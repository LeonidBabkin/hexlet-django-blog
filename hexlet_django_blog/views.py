from django.shortcuts import render

ARTICLES = [
    {'name': 'death-metal-bats', 'author': 'Elizabeth Rayne', 'link': 'https://www.livescience.com/death-metal-bats'},
    {'name': 'mind-controlled-wolves-toxoplasma-gondii', 'author': 'Joshua A. Krisch ', 'link': 'https://www.livescience.com/mind-controlled-wolves-toxoplasma-gondii'},
    {'name': 'wild-chimpanzees-and-gorillas-can-form-friendships', 'author': 'Chris Young', 'link': 'https://www.livescience.com/wild-chimpanzees-and-gorillas-can-form-friendships'},
    {'name': 'longest-living-animals', 'author': 'Patrick Pester', 'link': 'https://www.livescience.com/longest-living-animals.html'},
]


def index(request):
    return render(request, 'index.html')


def about(request):
    tags = ['обучение', 'программирование', 'python', 'oop']
    return render(
        request,
        'about.html',
        context={'tags': tags},


def details(request):
    return render(
        request,
        'details.html',
        context={'ARTICLES': ARTICLES},
    )
