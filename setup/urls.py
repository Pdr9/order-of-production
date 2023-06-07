from django.contrib import admin
from django.urls import path, include
from core.views import home, create
from django.conf.urls.static import static
from django.conf import settings
from real_time_production.views import exibir_pagina


urlpatterns = [
    path('admin/', admin.site.urls),
    path('inicio/', include('core.urls')),
    path('create/', create, name='create'),
    path('pagina/', exibir_pagina, name='exibir_pagina'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)