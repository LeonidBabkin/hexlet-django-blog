from django.contrib import admin
from .models import Category 
# Register your models here.

 
@admin.register(Category) 
class CategoryAdmin(admin.ModelAdmin): 
    list_display = ('name', 'description') # Перечисляем поля, отображаемые в таблице списка статей 
    search_fields = ['name', 'description'] 
