import decimal

from django.contrib import admin
from datetime import datetime as dt
from easy_select2 import select2_modelform

from .models import (
    Venta,
    VentaDetalle,
)
from modulos.producto.models import Producto

VentaDetalleForm = select2_modelform(VentaDetalle, attrs={'width': '400px'})


class VentaDetalleInline(admin.TabularInline):
    model = VentaDetalle
    form = VentaDetalleForm
    exclude = ('usuario_creacion', 'usuario_modificacion', 'usuario_eliminacion', 'fecha_modificacion',
               'fecha_eliminacion',)
    readonly_fields = ('subtotal',)
    extra = 0


@admin.register(Venta)
class VentaAdmin(admin.ModelAdmin):
    exclude = ('usuario_creacion', 'usuario_modificacion', 'usuario_eliminacion', 'fecha_modificacion',
               'fecha_eliminacion', 'venta_total')
    list_display = ('codigo_venta', 'razon_social', 'nit', 'fecha_venta', 'venta_total', 'usuario_creacion',)
    search_fields = ('codigo_venta', 'razon_social', 'nit', )
    inlines = [VentaDetalleInline, ]

    def save_model(self, request, obj, form, change):
        if change:
            obj.usuario_modificacion = request.user
            obj.fecha_modificacion = dt.now()
        else:
            obj.usuario_creacion = request.user
        obj.venta_total = 0
        super(VentaAdmin, self).save_model(request, obj, form, change)

    def save_formset(self, request, form, formset, change):
        instances = formset.save(commit=False)
        total = decimal.Decimal(0.0)
        venta_pk_tmp = 0
        try:
            for obj in formset.deleted_objects:
                obj.delete()
            for instance in instances:
                venta_pk_tmp = instance.venta_id
                total = total + (decimal.Decimal(instance.precio) * decimal.Decimal(instance.cantidad))
                instance.usuario_creacion = request.user
                instance.subtotal = (decimal.Decimal(instance.precio) * decimal.Decimal(instance.cantidad))
                producto = Producto.objects.get(pk=instance.producto_id)
                if producto.stock - instance.cantidad >= 0:
                    producto.stock = producto.stock - instance.cantidad
                    producto.save()
                    instance.save()
            formset.save_m2m()
            if venta_pk_tmp != 0:
                venta = Venta.objects.get(pk=venta_pk_tmp)
                venta.venta_total = total
                venta.save()
        except Exception as ex:
            print(ex)

    def delete_model(self, request, obj):
        obj.usuario_eliminacion = request.user
        obj.fecha_eliminacion = dt.now()
        obj.save()

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.filter(fecha_eliminacion__isnull=True)
        return queryset
