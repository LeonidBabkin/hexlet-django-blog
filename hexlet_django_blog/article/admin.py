from django.contrib import admin
from .models import Article

# Мы добавили класс, который описывает дополнительные свойства для отображения и работы с нашей моделью в разделе 
# администратора. В данном случае мы указали поле search_fields, в которое передали списком названия полей. 
# По ним будет осуществляться поиск.

class ArticleAdmin(admin.ModelAdmin):
        search_fields = ['name', 'body']
        
# Register your models here.
admin.site.register(Article, ArticleAdmin)


