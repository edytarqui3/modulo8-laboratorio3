from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin


class UserManager(BaseUserManager):
    def _create_user(self, username, email, documento, password, is_staff, is_superuser,
                     **extra_fields):
        user = self.model(
            username=username,
            email=email,
            documento=documento,
            is_staff=is_staff,
            is_superuser=is_superuser,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_user(self, username, email, documento, password=None, **extra_fields):
        return self._create_user(username, email, documento, password, False, False, **extra_fields)

    def create_superuser(self, username, email, documento, password=None, **extra_fields):
        return self._create_user(username, email, documento, password, True, True, **extra_fields)


class Usuario(AbstractBaseUser, PermissionsMixin):
    username = models.CharField('Nombre de usuario', max_length=50, unique=True)
    email = models.EmailField('Correo Electrónico', max_length=255, unique=True)
    documento = models.CharField('Nro. Documento', max_length=15, unique=True)
    nombre_completo = models.CharField('Nombre Completo', max_length=150, null=False, blank=False)
    cargo = models.CharField('Cargo', max_length=50)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'documento', ]

    def __str__(self):
        return self.username
