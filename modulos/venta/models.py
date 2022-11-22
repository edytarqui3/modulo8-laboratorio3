from django.db import models
from modulos.logmodel.models import LogModel
from modulos.producto.models import Producto


class Venta(LogModel):
    fecha_venta = models.DateField('Fecha de Venta')
    codigo_venta = models.CharField('Código de Venta', max_length=10, unique=True)
    razon_social = models.CharField('Razon Social', max_length=100)
    nit = models.CharField('Número de Identificación Tributaria', max_length=15)
    venta_total = models.DecimalField('Venta Total', max_digits=20, decimal_places=2)

    class Meta:
        verbose_name = 'Venta de Producto'
        verbose_name_plural = 'Ventas de Productos'

    def __str__(self):
        return f'{self.codigo_venta} ({self.razon_social} - {self.fecha_venta})'


class VentaDetalle(LogModel):
    venta = models.ForeignKey(Venta, related_name='+', on_delete=models.PROTECT)
    producto = models.ForeignKey(Producto, related_name='+', on_delete=models.PROTECT)
    precio = models.DecimalField('Costo del Producto $us', max_digits=10, decimal_places=2)
    cantidad = models.IntegerField('Cantidad', blank=False, null=False)
    subtotal = models.DecimalField('Total', max_digits=10, decimal_places=2)

    def __str__(self):
        return f'VENTA:{self.venta.codigo_venta}, PRODUCTO: {self.producto.producto} (TIPO: {self.producto.tipoproducto} - CATEGORIA: {self.producto.categoria})'
