from rest_framework import status
from rest_framework.response import Response

MESSAGE_SUCCESS = 'success'
MESSAGE_ERROR = 'error'
MESSAGE_WARNING = 'warning'


class Mensaje(object):
    """Mensajes enviados pueden ser de 3 tipos
    success: Para acciones con exito
    warning: Para acciones con peligro
    error: Para acciones erroreas
    """

    def __init__(self, tipo, mensaje, status=status.HTTP_200_OK):
        super(Mensaje, self).__init__()
        self.tipo = tipo
        self.mensaje = mensaje
        self.status = status

    def __dict__(self):
        diccionario = {
            'type': self.tipo,
            'message': self.mensaje,
            'status': self.status
        }
        return diccionario

    def render(self):
        return self.__dict__()

    def __unicode__(self):
        return self.mensaje


class ResponseMessage(Response):
    """
    Este es un mensaje que retorna con el tipo
    {
        "type":
        "code":
        "message":
        "data":
    }
    """

    def __init__(self, tipo='error', message='', status_code=status.HTTP_200_OK, data={}):
        valid_types = [MESSAGE_ERROR, MESSAGE_SUCCESS, MESSAGE_WARNING]
        if tipo not in valid_types:
            raise Exception('El tipo %s debe ser uno de los siguientes valores %s', (
                tipo,
                ','.join(x for x in valid_types)
            ))
        self.type = tipo
        self.message = message
        self.status = status_code
        self.data = data
        super(ResponseMessage, self).__init__(self.get_response(), status=self.status)

    def get_response(self):
        return {
            "type": self.type,
            "message": self.message,
            "status": self.status,
            "data": self.data
        }


def format_validation_errors(detail, html=False):
    """
    Se encarga de dar formato string a los errores de validaciones provenientes de los
    serializers

    :param detail: (dict) Detalle de los errores
    :param html: (bool) En caso que se quiera en string con formato html
    :return: (string)
    """
    if not isinstance(detail, dict):
        raise TypeError('The parameter detailt have to nedd a dict instance')
    message = ''
    for field in detail:
        for msg in detail[field]:
            if html:
                message += '<strong>%s</strong>: %s <br>' % (field.upper().replace('_', ' '), msg)
            else:
                message += '%s: %s\n' % (field.upper().replace('_', ' '), msg)
    return message
