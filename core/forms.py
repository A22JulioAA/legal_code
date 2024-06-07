from django import forms
from django.contrib.auth.forms import UserCreationForm
from users.models import Cliente

class RegistroForm(UserCreationForm):
    """
    Formulario para el registro de un usuario en la aplicación. Se basa en el modelo Cliente.
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
            'telefono': 'Telefono ',
        }
        widgets = {
            'password1': forms.PasswordInput(),
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date'}),
            'email': forms.EmailInput(attrs={'placeholder': 'correo@ejemplo.es', 'autocomplete': 'off'})
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['email'].widget.attrs['autocomplete'] = 'off' # Se desactiva el autocompletado que usa el navegador por defecto

class ModificarUsuarioForm(forms.ModelForm):
    """
    Formulario para la modificación de un usuario en la aplicación. Se basa en el modelo Cliente.
    Args:
        forms (ModelForm): Formulario que va a tener como base un Modelo creado
        
    """
    
    class Meta:
        model = Cliente # Se toma como modelo Cliente
        fields = ['name', 'apellidos', 'telefono', 'fecha_nacimiento', 'imagen_perfil']
        labels = {
            'name': 'Nombre ',
            'apellidos': 'Apellidos',
            'telefono': 'Telefono ',
            'fecha_nacimiento': 'Fecha de nacimiento ',
            'imagen_perfil': 'Imagen de perfil',
        }
        
        widgets = {
            'fecha_nacimiento': forms.DateInput(
                format='%d-%m-%Y',  
                attrs={'type': 'text', 'class': 'datepicker', 'autocomplete': 'off'},
            ),
            'imagen_perfil': forms.FileInput(attrs={'accept': 'image/*'}),
        }
        
        
        
    

