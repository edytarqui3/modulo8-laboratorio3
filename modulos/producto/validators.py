from django.core.exceptions import ValidationError


def validar_stock_minimo(value):
    if value < 10:
        raise ValidationError(
            '%(value)s stock minimo (10 unidades) esta por debajo de lo requerido',
            params={'value': value},
        )


def validar_costo_producto(value):
    if value < 0:
        raise ValidationError(
            '%(value)s no es un valor correcto para el costo del producto',
            params={'value': value},
        )
