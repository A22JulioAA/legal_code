from django import forms
from django.contrib.auth.forms import UserCreationForm
from users.models import Cliente

class RegistroForm(UserCreationForm):
    """

    Args:
        forms (ModelForm): Formulario que va a tener como base un Modelo creado
        
    """
    
    class Meta:
        model = Cliente # Se toma como modelo Cliente
        fields = ['name', 'apellidos','email', 'password1', 'password2', 'fecha_nacimiento']
        labels = {
            'name': 'Nombre ',
            'apellidos': 'Apellidos',
            'email': 'Correo ',
            'password1': 'Contraseña ',
            'fecha_nacimiento': 'Fecha de nacimiento ',
            'dni': 'DNI ',
            'telefono': 'Telefono ',
            'precio_consulta': 'Precio Consulta ',
            'direccion': 'Dirección '
        }
        widgets = {
            'password1': forms.PasswordInput(),
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date'})
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['email'].widget.attrs['autocomplete'] = 'off' # Se desactiva el autocompletado que usa el navegador por defecto
