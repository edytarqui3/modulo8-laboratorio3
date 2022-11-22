from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from .models import Usuario


class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar Contraseña', widget=forms.PasswordInput)

    class Meta:
        model = Usuario
        fields = ('username', 'documento', 'nombre_completo', 'cargo',
                  'is_active', 'is_superuser', 'is_staff', 'email',)

    def clean_email(self):
        username = self.cleaned_data.get('username')
        qs = Usuario.objects.filter(username=username)
        if qs.exists():
            raise forms.ValidationError("La Cuenta de usuario ya existe")
        return username

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("No coinciden las contraseñas")
        return password2


class UserAdminCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar contraseña', widget=forms.PasswordInput)

    class Meta:
        model = Usuario
        fields = ('username', 'documento', 'nombre_completo', 'cargo',
                  'is_active', 'is_superuser', 'is_staff', 'email',)

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("No coinciden las contraseñas")
        return password2

    def save(self, commit=True):
        user = super(UserAdminCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserAdminChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = Usuario
        fields = ('username', 'documento', 'nombre_completo', 'cargo',
                  'is_active', 'is_superuser', 'is_staff', 'email', 'password',)

    def clean_password(self):
        return self.initial["password"]
