from django.db import models

# Create your models here.
class Category(models.Model):
    STATE_TYPE = (
        ('draft', 'draft'),
        ('published', 'published')
    )
    name = models.CharField('name', max_length=255)
    description = models.CharField('description', max_length=255)
    state = models.CharField(choices=STATE_TYPE, max_length=9, default='draft')

    def __str__(self):
        """Represent model object."""
        return self.name
