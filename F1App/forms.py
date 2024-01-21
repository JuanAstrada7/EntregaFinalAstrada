from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from .models import Piloto, Carrera, Puntos

class PilotoForm(forms.ModelForm):
    class Meta:
        model = Piloto
        fields = ['nombre', 'equipo']

class CarreraForm(forms.ModelForm):
    class Meta:
        model = Carrera
        fields = ['piloto', 'posicion', 'vuelta_rapida']

class PuntosForm(forms.ModelForm):
    class Meta:
        model = Puntos
        fields = ['carrera', 'puntos']

class RegistrarUsuario(UserCreationForm):
    username = forms.CharField(label="ingrese su nombre de usuario")
    email = forms.EmailField(label="Correo Electronico")
    password1 = forms.CharField(label="Ingrese la Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repita la Contraseña", widget=forms.PasswordInput)
    first_name = forms.CharField(label="Ingrese su Nombre")
    last_name = forms.CharField(label="Ingrese su Apellido")

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2", "first_name", "last_name"]

class EditarUsuario(UserCreationForm):
    email = forms.EmailField(label="Correo Electronico")
    first_name = forms.CharField(label="Ingrese su Nombre")
    last_name = forms.CharField(label="Ingrese su Apellido")

    class Meta:
        model = User
        fields = ["email", "first_name", "last_name"]