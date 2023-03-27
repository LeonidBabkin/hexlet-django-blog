from django.shortcuts import render
from .forms import CommentArticleForm, CommentForm
from django.views import View
from hexlet_django_blog.article.models import Comment


class CommentArticleView(View):

    def get(self, request, *args, **kwargs):
        form = CommentArticleForm()  # Создаем экземпляр нашей формы
        return render(request, 'comment.html', {'form': form})  # Передаем нашу форму в контексте

    def post(self, request, *args, **kwargs):
        form = CommentArticleForm(request.POST)  # Получаем данные формы из запроса
        if form.is_valid():  # Проверяем данных формы на корректность
            comment = Comment(
                content=form.cleaned_data['content'],  # Получаем очищенные данные из поля content
                # created_at=form.cleaned_data['created_at'],
                # article=form.cleaned_data['article'],
            )
            comment.save()


class CommentFormView(View):

    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)  # Получаем данные формы из запроса
        if form.is_valid():  # Проверяем данных формы на корректность
            form.save()  # Сохраняем форму