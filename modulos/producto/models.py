from django.db import models
from modulos.logmodel.models import LogModel
from sorl.thumbnail import get_thumbnail
from django.utils.html import format_html
from .validators import (
    validar_costo_producto,
    validar_stock_minimo
)


class Categoria(LogModel):
    categoria = models.CharField('Categoria', max_length=50, unique=True)
    descripcion = models.TextField('Descripcion')

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.categoria


class Tipo(LogModel):
    tipoproducto = models.CharField('Tipo de Producto', max_length=50, unique=True)
    descripcion = models.CharField('Descripción', max_length=150)

    class Meta:
        verbose_name = 'Tipo de Producto'
        verbose_name_plural = 'Tipos de Productos'

    def __str__(self):
        return self.tipoproducto


class Producto(LogModel):
    categoria = models.ForeignKey(Categoria, related_name='+', on_delete=models.PROTECT)
    tipoproducto = models.ForeignKey(Tipo, related_name='+', on_delete=models.PROTECT)
    producto = models.CharField('Nombre del Producto', max_length=100,)
    descripcion = models.TextField('Descripción')
    imagen = models.ImageField('Imagen del Producto', upload_to='productos/', blank=False, null=False)
    stock = models.IntegerField('Stock del Producto', default=0, validators=[validar_stock_minimo, ])
    precio = models.DecimalField('Costo del Producto $us', decimal_places=2, max_digits=10, default=0,
                                 validators=[validar_costo_producto, ])
    estado = models.BooleanField('Estado Actual', default=True)

    @property
    def imagen_preview(self):
        if self.imagen:
            _imagen = get_thumbnail(self.imagen, '200x200', upscale=False, crop=False, quality=100)
            return format_html('<img src="{}" width="{}" height="{}">'.format(_imagen.url,
                                                                              _imagen.width,
                                                                              _imagen.height))
        return ""

    @property
    def imagen_tag(self):
        if self.imagen:
            _imagen = get_thumbnail(self.imagen, '55x55', upscale=False, crop=False, quality=100)
            return format_html('<img src="{}" width="{}" height="{}">'.format(_imagen.url,
                                                                              _imagen.width,
                                                                              _imagen.height))
        return ""

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

    def __str__(self):
        return f'{self.producto} ({self.tipoproducto} - {self.categoria})'
