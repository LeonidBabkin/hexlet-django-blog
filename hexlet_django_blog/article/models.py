
from django.db import models
from django.urls import reverse
from django.utils import timezone

# Create your models here.
class Article(models.Model):
    name = models.CharField(max_length=200) # название статьи
    body = models.TextField() # тело статьи
    created_at = models.DateTimeField(default=timezone.now)
# auto_now_add=True can be used as well
    
    def __str__(self):
        return self.name
