from django.urls import path
from hexlet_django_blog.articles import views


urlpatterns = [
    path('', IndexView.as_view(), name='app-views-articles'),
    path('<int:id>/', views.article_id, name='article_id'),
]
