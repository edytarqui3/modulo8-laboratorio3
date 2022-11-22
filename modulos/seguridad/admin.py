from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import UserAdminCreationForm, UserAdminChangeForm
from .models import Usuario


@admin.register(Usuario)
class UsuarioAdmin(BaseUserAdmin):
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm

    search_fields = ('username', 'documento', 'nombre_completo', 'cargo',)
    list_display = ('documento', 'username', 'nombre_completo', 'cargo', 'is_active')

    fieldsets = (
        (None, {'fields': ()}),
        ('Información Personal', {'fields': ('documento', 'nombre_completo',)}),
        ('Información Laboral', {'fields': (
            'cargo', 'email', 'username', 'password', 'is_active', 'is_staff', 'is_superuser')}),
        ('Grupos y Permisos', {'fields': ('groups',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('documento', 'nombre_completo', 'cargo', 'email', 'username',
                       'password1', 'password2', 'is_active', 'is_staff', 'is_superuser', )}
         ),
    )