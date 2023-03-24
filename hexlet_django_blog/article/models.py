
from django.db import models
from django.urls import reverse

# Create your models here.
class Article(models.Model):
    name = models.CharField(max_length=200) # название статьи
    body = models.TextField() # тело статьи
    timestamp = models.DateTimeField(auto_now_add=True)
  

def get_absolute_urls(self,):
    return reverse('article', args=[self.pk])
    

 
