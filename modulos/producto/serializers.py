from rest_framework import serializers
from .models import (
    Categoria,
    Producto,
    Tipo
)


class TipoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Tipo
        fields = ('id', 'tipoproducto', 'descripcion', )


class CategoriaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ('id', 'categoria', 'descripcion', )


class ProductoSerializers(serializers.ModelSerializer):
    categoria = CategoriaSerializers(read_only=True)
    categoria_id = serializers.IntegerField()
    tipoproducto = TipoSerializers(read_only=True)
    tipoproducto_id = serializers.IntegerField()
    
    class Meta:
        model = Producto
        fields = (
            'id', 'categoria', 'categoria_id', 'tipoproducto', 'tipoproducto_id',
            'producto', 'descripcion', 'imagen', 'stock', 'precio', 'estado'
        )
