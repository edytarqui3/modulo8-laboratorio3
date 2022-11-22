import decimal

from django.contrib import admin
from datetime import datetime as dt
from easy_select2 import select2_modelform

from .models import (
    Ingreso,
    IngresoDetalle,
)
from modulos.producto.models import Producto

IngresoDetalleForm = select2_modelform(IngresoDetalle, attrs={'width': '400px'})


class IngresoDetalleInline(admin.TabularInline):
    model = IngresoDetalle
    form = IngresoDetalleForm
    exclude = ('usuario_creacion', 'usuario_modificacion', 'usuario_eliminacion', 'fecha_modificacion',
               'fecha_eliminacion',)
    extra = 0


@admin.register(Ingreso)
class IngresoAdmin(admin.ModelAdmin):
    exclude = ('usuario_creacion', 'usuario_modificacion', 'usuario_eliminacion', 'fecha_modificacion',
               'fecha_eliminacion', 'costo_total')
    list_display = ('codigo_ingreso', 'descripcion', 'fecha_ingreso', 'costo_total', 'fecha_creacion', 'usuario_creacion',)
    search_fields = ('codigo_ingreso', 'descripcion', 'fecha_ingreso', )
    inlines = [IngresoDetalleInline, ]

    def save_model(self, request, obj, form, change):
        if change:
            obj.usuario_modificacion = request.user
            obj.fecha_modificacion = dt.now()
        else:
            obj.usuario_creacion = request.user
        obj.costo_total = 0
        super(IngresoAdmin, self).save_model(request, obj, form, change)

    def save_formset(self, request, form, formset, change):
        instances = formset.save(commit=False)
        total = decimal.Decimal(0.0)
        ingreso_pk_tmp = 0
        try:
            for obj in formset.deleted_objects:
                obj.delete()
            for instance in instances:
                ingreso_pk_tmp = instance.ingreso_id
                total = total + (decimal.Decimal(instance.precio) * decimal.Decimal(instance.cantidad))
                instance.usuario_creacion = request.user
                producto = Producto.objects.get(pk=instance.producto_id)
                producto.precio = instance.precio
                producto.stock = producto.stock + instance.cantidad
                producto.save()
                instance.save()
            formset.save_m2m()
            if ingreso_pk_tmp != 0:
                ingreso = Ingreso.objects.get(pk=ingreso_pk_tmp)
                ingreso.costo_total = total
                ingreso.save()
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
