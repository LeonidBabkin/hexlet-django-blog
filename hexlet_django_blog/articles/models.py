from django.db import models
import django.utils.timezone
from hexlet_django_blog.categories.models import Category


# Create your models here.
class Article(models.Model):
    title = models.CharField('title', max_length=255)
    body = models.CharField('body', max_length=255)
    created_at = models.DateField('created_at', default=timezone.now)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)

    def __str__(self):
        """Represent model object."""
        return self.title
