from django.db import models
from django.urls import reverse

# Create your models here.
class Article(models.Model):
  title = models.TextField()
  content = models.TextField()
  
  
  def get_absolute_urls(self,):
      return reverse('article', args=[self.pk])
    

 
