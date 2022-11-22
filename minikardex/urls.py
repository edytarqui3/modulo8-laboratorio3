from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
import modulos.producto.urls as urls_productos

urlpatterns = [
    path('minikardex/', admin.site.urls),
    path('api/producto/', include(urls_productos), name='urls_producto'),
]


# Titulo del Header
admin.site.site_header = 'MINIKARDEX'
admin.site.site_title = 'MINIKARDEX'
admin.site.index_title = 'APP MINIKARDEX'

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

