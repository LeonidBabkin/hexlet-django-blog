from django.forms import ModelForm
from django import forms
from hexlet_django_blog.categories.models import Category


class CategoryForm(forms.ModelForm):  # переопределяем модель
    name = forms.CharField(max_length=100, required=True)
    description = forms.CharField(max_length=200, required=True)

    class Meta:
        model = Category
        fields = ['name', 'description', 'state']