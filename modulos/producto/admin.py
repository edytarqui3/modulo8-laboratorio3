import csv
from django.contrib import admin
from datetime import datetime as dt
from django.http import HttpResponse
from easy_select2 import select2_modelform

from .models import (
    Categoria,
    Tipo,
    Producto,
)

ProductoForm = select2_modelform(Producto, attrs={'width': '400px'})


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    exclude = ('usuario_creacion', 'usuario_modificacion', 'usuario_eliminacion', 'fecha_modificacion',
               'fecha_eliminacion',)
    list_display = ('categoria', 'descripcion', 'fecha_creacion', 'usuario_creacion',)
    search_fields = ('categoria', 'descripcion', )

    def save_model(self, request, obj, form, change):
        if change:
            obj.usuario_modificacion = request.user
            obj.fecha_modificacion = dt.now()
        else:
            obj.usuario_creacion = request.user
        super(CategoriaAdmin, self).save_model(request, obj, form, change)

    def delete_model(self, request, obj):
        obj.usuario_eliminacion = request.user
        obj.fecha_eliminacion = dt.now()
        obj.save()

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.filter(fecha_eliminacion__isnull=True)
        return queryset


@admin.register(Tipo)
class TipoAdmin(admin.ModelAdmin):
    exclude = ('usuario_creacion', 'usuario_modificacion', 'usuario_eliminacion', 'fecha_modificacion',
               'fecha_eliminacion',)
    list_display = ('tipoproducto', 'descripcion', 'fecha_creacion', 'usuario_creacion',)
    search_fields = ('tipoproducto', 'descripcion', )

    def save_model(self, request, obj, form, change):
        if change:
            obj.usuario_modificacion = request.user
            obj.fecha_modificacion = dt.now()
        else:
            obj.usuario_creacion = request.user
        super(TipoAdmin, self).save_model(request, obj, form, change)

    def delete_model(self, request, obj):
        obj.usuario_eliminacion = request.user
        obj.fecha_eliminacion = dt.now()
        obj.save()

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.filter(fecha_eliminacion__isnull=True)
        return queryset


class ExportarCsvMixin:
    def export_a_csv(self, request, queryset):
        meta = self.model._meta
        field_names = [field.name for field in meta.fields]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in field_names])

        return response

    export_a_csv.short_description = "Exportar Seleccionados"


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin, ExportarCsvMixin):
    form = ProductoForm
    exclude = ('usuario_creacion', 'usuario_modificacion', 'usuario_eliminacion', 'fecha_modificacion',
               'fecha_eliminacion',)
    list_display = ('producto', 'categoria', 'tipoproducto', 'imagen_tag', 'precio', 'stock', 'estado', 'fecha_creacion',
                    'usuario_creacion',)
    search_fields = ('categoria', 'tipoproducto', 'producto', 'descripcion', 'precio',)
    readonly_fields = ('imagen_preview',)

    def imagen_preview(self, obj):
        return obj.imagen_preview

    def imagen_tag(self, obj):
        return obj.imagen_tag

    def save_model(self, request, obj, form, change):
        if change:
            obj.usuario_modificacion = request.user
            obj.fecha_modificacion = dt.now()
        else:
            obj.usuario_creacion = request.user
        super(ProductoAdmin, self).save_model(request, obj, form, change)

    def delete_model(self, request, obj):
        obj.usuario_eliminacion = request.user
        obj.fecha_eliminacion = dt.now()
        obj.save()

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.filter(fecha_eliminacion__isnull=True)
        return queryset

    actions = ['export_a_csv', ]
