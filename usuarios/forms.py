from django import forms
from .models import Especialidad

class RegistroClienteForm(forms.Form):
    nombre = forms.CharField(label = 'Nombre ', max_length=100, required=True, widget=forms.TextInput(attrs={}))
    apellidos = forms.CharField(label = 'Apellidos ', max_length=100, required=False, widget=forms.TextInput(attrs={}))
    email = forms.EmailField(label = 'Email ', max_length=100, required=True)
    password = forms.CharField(label = 'Password ', max_length = 100, required=True, widget=forms.PasswordInput(attrs={}))
    fecha_nacimiento = forms.DateField(label = 'Fecha de Nacimiento ', required=True, widget=forms.DateInput(attrs={'type': 'date'}))
    telefono = forms.CharField(label = 'Teléfono ', max_length=15, required=False, widget=forms.TextInput(attrs={'type': 'tel', 'placeholder': '+34'}))    

class RegistroProfesionalForm(forms.Form):
    nombre = forms.CharField(label = 'Nombre ', max_length=100, required=True, widget=forms.TextInput(attrs={}))
    apellidos = forms.CharField(label = 'Apellidos ', max_length=100, required=False, widget=forms.TextInput(attrs={}))
    email = forms.EmailField(label = 'Email ', max_length=100, required=True)
    password = forms.CharField(label = 'Password ', max_length = 100, required=True, widget=forms.PasswordInput(attrs={}))
    dni = forms.CharField(label = 'DNI ', max_length=9, required=True, widget=forms.TextInput(attrs={'pattern': '[0-9]{8}[A-Za-z]', 'title': 'xxxxxxxx0'}))
    fecha_nacimiento = forms.DateField(label = 'Fecha de Nacimiento ', required=True, widget=forms.DateInput(attrs={'type': 'date'}))
    telefono = forms.CharField(label = 'Teléfono ', max_length=15, required=True, widget=forms.TextInput(attrs={'type': 'tel', 'placeholder': '+34'}))
    especialidad = forms.ModelChoiceField(queryset=Especialidad.objects.all())
    direccion = forms.CharField(label = 'Dirección: ', max_length=200, required=True, widget=forms.TextInput(attrs={}))
    precio_consulta = forms.FloatField(label = 'Precio Consulta ', min_value=0, required=False, widget=forms.NumberInput(attrs={'placeholder': '€'}))

class LoginClienteForm(forms.Form):
    email = forms.EmailField(label = 'Email ', max_length=100, required=True)
    password = forms.CharField(label = 'Contraseña ', max_length=100, required=True)   

class LoginProfesionalForm(forms.Form):
    email = forms.EmailField(label = 'Email ', max_length=100, required=True)
    password = forms.CharField(label = 'Contraseña ', max_length=100, required=True)