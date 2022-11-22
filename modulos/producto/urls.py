from rest_framework.routers import DefaultRouter
from .views import (
    TipoViewsets,
    CategoriaViewsets,
    ProductoViewsets
)

api_router = DefaultRouter()

api_router.register('tipoproducto', TipoViewsets, 'tipo')
api_router.register('categoria', CategoriaViewsets, 'categoria')
api_router.register('producto', ProductoViewsets, 'producto')

urlpatterns = api_router.urls
