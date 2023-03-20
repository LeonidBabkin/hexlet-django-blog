from django.shortcuts import render
from django.views.generic.base import TemplateView

ARTICLES = [
    {'name': 'death-metal-bats', 'author': 'Elizabeth Rayne', 'link': 'https://www.livescience.com/death-metal-bats'},
    {'name': 'mind-controlled-wolves-toxoplasma-gondii', 'author': 'Joshua A. Krisch ', 'link': 'https://www.livescience.com/mind-controlled-wolves-toxoplasma-gondii'},
    {'name': 'wild-chimpanzees-and-gorillas-can-form-friendships', 'author': 'Chris Young', 'link': 'https://www.livescience.com/wild-chimpanzees-and-gorillas-can-form-friendships'},
    {'name': 'longest-living-animals', 'author': 'Patrick Pester', 'link': 'https://www.livescience.com/longest-living-animals.html'},
]

#  Переделайте hexlet_django_blog.views.index с использованием TemplateView. View должна наследовать этот класс,
#  а не быть заменена на TemplateView.as_view(…)

class IndexView(TemplateView):
    template_name = "index.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['who'] = 'World'
        return context

def about(request):
    tags = ['обучение', 'программирование', 'python', 'oop']
    return render(
        request,
        'about.html',
        context={'tags': tags},
    )


# def details(request):
#     return render(
#         request,
#         'details.html',
#         context={'ARTICLES': ARTICLES},
#     )

class DetailsView(TemplateView):
    template_name = "details.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context={'ARTICLES': ARTICLES}
        return context
