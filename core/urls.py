from django.contrib import admin
from django.urls import path, include
from .views import home, salvar, editar, update, delete, create

urlpatterns = [
    path('', home, name='home'),
    path('create/', create, name='create'),
    path('salvar', salvar, name="salvar"),
    path('editar/<int:id>', editar, name='editar'),
    path('update/<int:id>', update, name='update'),
    path('delete/<int:id>', delete, name='delete'),
] 
