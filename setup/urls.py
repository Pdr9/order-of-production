from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from core.views import create, exibir_pagina

urlpatterns = [
    path('admin/', admin.site.urls),
    path('create/', create, name='create'),
    path('pagina/', exibir_pagina, name='exibir_pagina'),
]

for month in range(1, 13):
    urlpatterns += [
        path(f'op/{month}/', include('core.urls')),
    ]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
