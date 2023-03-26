from django.contrib import admin
from .models import Article 

# Register your models here.
# admin.site.register(Article)

# class ArticleAdmin(admin.ModelAdmin): 
#     search_fields = ['name', 'body'] 
 
# admin.site.register(Article, ArticleAdmin) 
@admin.register(Article) 
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('name', 'timestamp')
    search_fields = ['name', 'body']
    list_filter = (('created_at', DateFieldListFilter),)
    

