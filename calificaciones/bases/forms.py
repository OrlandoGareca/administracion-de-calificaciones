from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from calificaciones.users.models import User
#from calificaciones.users.forms import UserCreationForm


class RegisterForm(forms.ModelForm):
    name = forms.CharField(max_length=50,label="Nombres",widget=forms.TextInput)
    apellido = forms.CharField(max_length=50,label='apellidos',widget=forms.TextInput)
    phone = forms.CharField(max_length=8,label="Telefono",widget=forms.TextInput)
    dni = forms.CharField(max_length=10,label="Cedula de Identidad",widget=forms.TextInput)
    email = forms.EmailField(label='Correo Electronico', widget=forms.EmailInput)
    date_of_birth = forms.DateField(label='Fecha de Nacimiento',widget=forms.DateInput)


    class Meta:
        model = User

        fields = ('name','apellido','dni','phone','email','date_of_birth','picture')

