from django import forms
from .models import Cita

class CitaForm(forms.ModelForm):
    '''
        Este formulario se utiliza para crear nuevas citas. Contiene campos para la descripción de la cita y la fecha de la cita.
    '''

    class Meta:
        model = Cita
        fields = ['descripcion', 'fecha_cita']
        
        labels = {
            'descripcion': 'Motivo de la cita: ',
            'fecha_cita': 'Fecha de la cita: ',
        }

        widgets = {
            'descripcion': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Describe brevemente el motivo de la cita...'}),
            'fecha_cita': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }