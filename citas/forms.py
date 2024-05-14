from django import forms
from .models import Cita

class CitaForm(forms.ModelForm):
    class Meta:
        model = Cita
        fields = ['descripcion', 'fecha_cita', 'precio']

        widgets = {
            'descripcion': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Describe brevemente el motivo de la cita...'}),
            'fecha_cita': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'precio': forms.TextInput(attrs={'type': 'number', 'min': 0}),
        }