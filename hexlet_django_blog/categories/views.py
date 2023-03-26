from django.shortcuts import get_object_or_404, render
from django.views import View
from hexlet_django_blog.categories.models import Category


class IndexView(View):

    def get(self, request, *args, **kwargs):
        categories = Category.objects.all()
        return render(request, 'categories/index.html', context={
            'categories': categories,
        })


# BEGIN (write your solution here) Task 13
class CategoryView(View):
    template_name = 'categories/category.html'

    def get(self, request, *args, **kwargs):
        category = get_object_or_404(Category, id=kwargs['id'])
        return render(request, self.template_name, context={
            'category': category,
        })
# END
