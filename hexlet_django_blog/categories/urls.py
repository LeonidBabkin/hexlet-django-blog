from django.urls import path
from hexlet_django_blog.categories import views


urlpatterns = [
    path('', views.IndexView.as_view(), name='categories_index'),
    path('<int:id>/', views.CategoryView.as_view(), name='categories_detail'),
    path(
        'create/',
        views.CategoryFormCreateView.as_view(),
        name='category_create'
    )
]
