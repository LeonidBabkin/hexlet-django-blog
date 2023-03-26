from django.db import models
from hexlet_django_blog.categories.models import Category


# Create your models here.
class Article(models.Model):
    title = models.CharField('title', max_length=255)
    body = models.CharField('body', max_length=255)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)

    def __str__(self):
        """Represent model object."""
        return self.title
