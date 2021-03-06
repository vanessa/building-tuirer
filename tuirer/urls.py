from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from core.views import index

# Todas as nossas URLs do projeto estarão aqui.
# O Django sabe que esse é o arquivo principal
# de URLs por causa de uma variável nos arquivos
# de configuração chamada `ROOT_URLCONF`.

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),

    path('', include('tuites.urls')),
    path('', include('users.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
