# Generated by Django 4.1.7 on 2023-04-07 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_article_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='body',
            field=models.CharField(max_length=1000, verbose_name='body'),
        ),
    ]
