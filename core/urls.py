from django.contrib import admin
from django.urls import path, include
from .views import home, update, delete, create
from real_time_production.views import exibir_pagina

urlpatterns = [
    path('', home, name='home'),
    path('create/', create, name='create'),
    path('update/<int:id>', update, name='update'),
    path('delete/<int:id>', delete, name='delete'),
    path('pagina/', exibir_pagina, name='exibir_pagina'),
]
