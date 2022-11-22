from modulos.logmodel.viewsets import RestLogModelViewSet
from .models import (
    Tipo,
    Categoria,
    Producto
)
from .serializers import (
    TipoSerializers,
    CategoriaSerializers,
    ProductoSerializers
)


class TipoViewsets(RestLogModelViewSet):
    model = Tipo
    serializer_class = TipoSerializers
    queryset = Tipo.objects.filter(fecha_eliminacion__isnull=True)


class CategoriaViewsets(RestLogModelViewSet):
    model = Categoria
    serializer_class = CategoriaSerializers
    queryset = Categoria.objects.filter(fecha_eliminacion__isnull=True)


class ProductoViewsets(RestLogModelViewSet):
    model = Producto
    serializer_class = ProductoSerializers
    queryset = Producto.objects.filter(fecha_eliminacion__isnull=True)
