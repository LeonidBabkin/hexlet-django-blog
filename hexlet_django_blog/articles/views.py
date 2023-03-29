from django.shortcuts import get_object_or_404, render, redirect
from django.views import View
from hexlet_django_blog.articles.models import Article
from django.db.models import Q
from hexlet_django_blog.articles.forms import ArticleForm
from django.contrib import messages
# в любом случае работает фильтрация
# если не пользуешься формой, то фильтруешь все статьи которые содержат
# пустую строку "". А пустую строку содержит любая строка поэтому фильтр
# возвращает из БД все.
class IndexView(View):

    def get(self, request, *args, **kwargs):
        query = request.GET.get('q', '')  # извлечение запроса из формы: "Get the value of a GET variable with name
        # 'q', and if it doesn't exist, return ''.
        articles = Article.objects.filter(Q(title__icontains=query))  # поиск в названиях статей в соответсвии с
        # запросом
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

# В данном get-обработчике мы создаем объект формы и передаем его в шаблон:
class ArticleFormCreateView(View):

    def get(self, request, *args, **kwargs):
        form = ArticleForm()
        return render(request, 'articles/create.html', {'form': form})


    def post(self, request, *args, **kwargs):
        form = ArticleForm(request.POST)
        if form.is_valid():  # Если данные корректные, то сохраняем данные формы
            form.save()
            messages.success(request, "Статья добавлена")
            return redirect('/articles/')  # Редирект на указанный маршрут
        # Если данные некоректные, то возвращем человека обратно на страницу с заполенной формой
        messages.error(request, 'Статья неверна. Попробуйте снова')
        return render(request, 'articles/create.html', {'form': form})