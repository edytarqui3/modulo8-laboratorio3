from datetime import datetime as dt
from django.core.exceptions import ValidationError as ModelValidationError
from rest_framework.exceptions import ValidationError
from django.db import DatabaseError
from rest_framework.viewsets import ModelViewSet as DefaultModelViewSet, ViewSet as DefaultViewSet
from rest_framework import status

from .response import SuccessRestResponse, ErrorRestResponse


class ViewSet(DefaultViewSet):
    pass


class ModelViewSet(DefaultModelViewSet):
    pass


class GenericModelViewSet(ModelViewSet):
    def create(self, request, *args, **kwargs):
        request.data['fecha_creacion'] = dt.now()
        return super(GenericModelViewSet, self).create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        request.data['fecha_modificacion'] = dt.now()
        return super(GenericModelViewSet, self).update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        object = self.get_object()
        object.fecha_eliminacion = dt.now()
        object.save()
        return SuccessRestResponse('Eliminado')


class RestLogModelViewSet(ModelViewSet):
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
        except ModelValidationError as ex:
            return ErrorRestResponse(
                message=ex.messages[0],
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
        except ValidationError as ex:
            return ErrorRestResponse(
                message='Se presentaron los siguientes errores',
                data=ex.detail,
                status=status.HTTP_400_BAD_REQUEST
            )
        except DatabaseError as ex:
            return ErrorRestResponse(message=str(ex))
        return SuccessRestResponse(
            message='%s creado(a)' % self.model._meta.verbose_name,
            data=serializer.data,
            status=status.HTTP_201_CREATED
        )

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)
        except ModelValidationError as ex:
            return ErrorRestResponse(
                message=ex.messages[0],
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
        except ValidationError as ex:
            return ErrorRestResponse(
                message='Se presentaron los siguientes errores',
                data=ex.detail,
                status=status.HTTP_400_BAD_REQUEST
            )
        except DatabaseError as ex:
            return ErrorRestResponse(message=ex.message)

        if getattr(instance, '_prefetched_objects_cache', None):
            instance = self.get_object()
            serializer = self.get_serializer(instance)
        else:
            instance = self.get_object()
            serializer = self.get_serializer(instance)

        return SuccessRestResponse(
            message='%s modificado(a)' % self.model._meta.verbose_name,
            data=serializer.data,
        )

    def destroy(self, request, *args, **kwargs):
        object = self.get_object()
        object.fecha_eliminacion = dt.now()
        object.save()
        return SuccessRestResponse(
            message=('%s eliminado(a)' % self.model._meta.verbose_name)
        )

    def perform_create(self, serializer):
        serializer.save(fecha_creacion=dt.now())

    def perform_update(self, serializer):
        serializer.save(fecha_modificacion=dt.now())

