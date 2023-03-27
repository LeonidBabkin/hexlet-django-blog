from django import forms  # Импортируем формы Django
from django.forms import ModelForm
from hexlet_django_blog.article.models import Article


class CommentArticleForm(forms.Form):
    content = forms.CharField(label='Комментарий')  # Текст комментария


# class ArticleForm(ModelForm):
#     class Meta:
#         model = Article
#         fields = ['title', 'body']