from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('authors/', views.authors, name='authors'),
    path('categories/', views.categories, name='categories'),
    path('subcategories/', views.subcategories, name='subcategories'),
    path('going-read/', views.going_read, name='going-read'),
    path('helpful-resources/', views.helpful_resources, name='helpful-resources'),
]