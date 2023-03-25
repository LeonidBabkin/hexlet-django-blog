from django.contrib import admin
from .models import Article
from django.contrib.admin import DateFieldListFilter

# Мы добавили класс, который описывает дополнительные свойства для отображения и работы с нашей моделью в разделе 
# администратора. В данном случае мы указали поле search_fields, в которое передали списком названия полей. 
# По ним будет осуществляться поиск.

# class ArticleAdmin(admin.ModelAdmin):
#         search_fields = ['name', 'body']
        
# # Register your models here.
# admin.site.register(Article, ArticleAdmin)


# Мы можем улучшить читаемость нашего кода, если воспользуемся декоратором @admin.register(). 
# Он позволяет связать модель с классом и провести регистрацию модели в разделе администратора:
# Еще добавим отображение в списке статей даты публикации и фильтрацию по данному полю:

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):  
        list_display = ('name', 'timestamp') # Перечисляем поля, отображаемые в таблице списка статей
        search_fields = ['name', 'body']
        list_filter = (('created_at', DateFieldListFilter),) # Перечисляем поля для фильтрации
