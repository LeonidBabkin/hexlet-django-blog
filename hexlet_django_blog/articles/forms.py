from django.forms import ModelForm
from .models import Article

# Форма описывает поля существующей модели Article. Поэтому для описания формы
# воспользуемся вспомогательным классом ModelForm, чтобы создать Form-класс из
# модели Django:
class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'body', 'category']