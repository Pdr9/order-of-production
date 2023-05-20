from django.contrib import admin
from django.urls import path, include
from .views import home, update, delete, create

urlpatterns = [
    path('', home, name='home'),
    path('create/', create, name='create'),
    path('update/<int:id>', update, name='update'),
    path('delete/<int:id>', delete, name='delete'),
] 
