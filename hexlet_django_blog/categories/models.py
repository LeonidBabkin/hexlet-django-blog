from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField('name', max_length=255)
    description = models.CharField('description', max_length=255)

    def __str__(self):
        """Represent model object."""
        return self.name
