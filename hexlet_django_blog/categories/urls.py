from django.urls import path
from simple_blog.categories import views


urlpatterns = [
    path('', views.categories),
]
