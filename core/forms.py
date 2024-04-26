from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profesional

# class CustomUserCreationForm(UserCreationForm):
#     class Meta:
#         model = User
#         fields = ['username', 'password', 'email']

class CustomUserCreationForm(forms.ModelForm):
    class Meta:
        model = Profesional
        fields = ['nombre', 'email', 'password']
        labels = {
            'nombre': 'Nombre ',
            'email': 'Correo ',
            'password': 'Contraseña '
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['email'].widget.attrs['autocomplete'] = 'off'
