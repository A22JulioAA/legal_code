from django import forms
from .models import Cita

class CitaForm(forms.ModelForm):
    class Meta:
        model = Cita
        fields = ['profesional', 'cliente', 'descripcion', 'fecha_cita', 'precio']

        widgets = {
            'descripcion': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Describe brevemente el motivo de la cita...'}),
            'fecha_cita': forms.TextInput(attrs={'type': 'date'}),
            'precio': forms.TextInput(attrs={'type': 'number', 'value': 50, 'min': 0}),
        }