from django.db import models
from django.utils import timezone
from hexlet_django_blog.articles.models import Article


class Comment(models.Model):
    content = models.CharField('content', max_length=255)
    # created_at = models.DateField('created_at', default=timezone.now)
    # article = models.ForeignKey(Article, on_delete=models.PROTECT)

    def __str__(self):
        """Represent model object."""
        return self.content
