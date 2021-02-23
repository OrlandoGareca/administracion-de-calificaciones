from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from calificaciones.users.models import User
from django.core.exceptions import ValidationError
# from calificaciones.users.forms import UserCreationForm


class RegisterForm(forms.ModelForm):
    name = forms.CharField(max_length=50, label="Nombres", widget=forms.TextInput)
    apellido = forms.CharField(max_length=50, label='apellidos', widget=forms.TextInput)
    phone = forms.CharField(max_length=8, label="Telefono", widget=forms.TextInput)
    dni = forms.CharField(max_length=10, label="Cedula de Identidad", widget=forms.TextInput)
    email = forms.EmailField(label='Correo Electronico', widget=forms.EmailInput)
    date_of_birth = forms.DateField(label='Fecha de Nacimiento', widget=forms.DateInput)

    class Meta:
        model = User
        fields = ('name', 'apellido', 'dni', 'phone', 'email', 'date_of_birth', 'picture')

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if len(name) > 30:
            raise forms.ValidationError("Los nombres tiene que tener maximo 30 caracteres")
        return name
    def clean_apellido(self):
        apellido = self.cleaned_data.get('apellido')
        if len(apellido) > 30:
            raise forms.ValidationError("Los Apellidos tienen que tener maximo 30 caracteres")
        return apellido

    def clean_dni(self):
        dni = self.cleaned_data.get('dni')
        if len(str(dni)) > 10:
            raise forms.ValidationError("El numero de DNI tiene que tener maximo 10 caracteres")
        else:
            if User.objects.filter(dni=dni).exists():
                raise forms.ValidationError("DNI ya existe")
        return dni
    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if len(str(phone)) > 8:
            raise forms.ValidationError("El nunero de telefono tiene que ser maximo 8 caracteres")
        return phone
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if len(str(email)) < 10:
            raise forms.ValidationError("Introdusca un correo electronico valido")
        else:
            if User.objects.filter(email=email).exists():
                raise forms.ValidationError("Correo electronico ya existe")
        return email

    def clean_date_of_birth(self):
        date_of_birth = self.cleaned_data.get('date_of_birth')
        if len(str(date_of_birth)) > 10:
            raise forms.ValidationError("Introdusca una fecha valida")
        return date_of_birth


