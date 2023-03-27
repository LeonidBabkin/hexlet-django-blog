from django import forms  # Импортируем формы Django
from django.forms import ModelForm
from hexlet_django_blog.article.models import Comment


class CommentArticleForm(forms.Form):
    content = forms.CharField(label='Комментарий')  # Текст комментария


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['content']