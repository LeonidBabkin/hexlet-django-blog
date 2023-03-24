
from django.db import models
from django.urls import reverse

# Create your models here.
class Article(models.Model):
    name = models.CharField(max_length=200) # название статьи
    body = models.TextField() # тело статьи
    created_at = models.DateTimeField(auto_now_add=True)

    
    def __str__(self):
        return self.name
