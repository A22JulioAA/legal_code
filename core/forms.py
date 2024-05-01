from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profesional

class CustomUserCreationForm(forms.ModelForm):
    """

    Args:
        forms (ModelForm): Formulario que va a tener como base un Modelo creado
        
    """
    
    class Meta:
        model = Profesional # Se toma como modelo Profesional
        fields = ['nombre', 'apellidos','email', 'password', 'fecha_nacimiento', 'dni', 'telefono', 'precio_consulta', 'direccion']
        labels = {
            'nombre': 'Nombre ',
            'apellidos': 'Apellidos',
            'email': 'Correo ',
            'password': 'Contraseña ',
            'fecha_nacimiento': 'Fecha de nacimiento ',
            'dni': 'DNI ',
            'telefono': 'Telefono ',
            'precio_consulta': 'Precio Consulta ',
            'direccion': 'Dirección '
        }
        widgets = {
            'password': forms.PasswordInput(),
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date'})
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['email'].widget.attrs['autocomplete'] = 'off' # Se desactiva el autocompletado que usa el navegador por defecto
