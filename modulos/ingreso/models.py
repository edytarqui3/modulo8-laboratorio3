from django.db import models
from modulos.logmodel.models import LogModel
from modulos.producto.models import Producto


class Ingreso(LogModel):
    fecha_ingreso = models.DateField('Fecha de Ingreso')
    codigo_ingreso = models.CharField('Código de Ingreso', max_length=10, unique=True)
    descripcion = models.CharField('Descripción', max_length=100)
    costo_total = models.DecimalField('Costo Total', max_digits=20, decimal_places=2)

    class Meta:
        verbose_name = 'Ingreso de Producto'
        verbose_name_plural = 'Ingresos de Productos'

    def __str__(self):
        return f'{self.descripcion} ({self.fecha_ingreso})'


class IngresoDetalle(LogModel):
    ingreso = models.ForeignKey(Ingreso, related_name='+', on_delete=models.PROTECT)
    producto = models.ForeignKey(Producto, related_name='+', on_delete=models.PROTECT)
    precio = models.DecimalField('Costo del Producto $us', max_digits=10, decimal_places=2)
    cantidad = models.IntegerField('Cantidad', blank=False, null=False)

    def __str__(self):
        return f'{self.producto.producto} (TIPO: {self.producto.tipoproducto} - CATEGORIA: {self.producto.categoria})'
