from django import forms
from .models import Comentario

class CrearComentarioForm(forms.ModelForm):
    '''
        Este modelo establece los campos del formulario de los comentarios.
    '''
    class Meta:
        model = Comentario
        fields = ['texto_comentario', 'recomendacion', 'valoracion']
        labels = {
            'texto_comentario': 'Escribe tu comentario: ',
            'recomendacion': '¿Recomendarías a este profesional?',
            'valoracion': 'Valora tu experiencia(1-5):'
        }
        widgets = {
            'texto_comentario': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'valoracion': forms.NumberInput(attrs={'class': 'rating', 'min': 1, 'max': 5}),
            'recomendacion': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }