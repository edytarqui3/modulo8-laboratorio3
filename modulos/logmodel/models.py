from __future__ import unicode_literals
from django.db import models
from django.conf import settings


class LogModel(models.Model):
    """Modelo que implementa los campos de log creacion, modificacion, eliminacion"""
    usuario_creacion = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='+',
        on_delete=models.PROTECT
    )
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    usuario_modificacion = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='+',
        null=True,
        blank=True,
        on_delete=models.PROTECT
    )
    fecha_modificacion = models.DateTimeField(null=True, blank=True)
    usuario_eliminacion = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='+',
        null=True,
        blank=True,
        on_delete=models.PROTECT
    )
    fecha_eliminacion = models.DateTimeField(null=True, blank=True)

    class Meta:
        abstract = True
