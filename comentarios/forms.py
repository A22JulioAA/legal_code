from django import forms
from usuarios.models import Profesional, Cliente

class CrearComentarioForm(forms.Form):
    profesional = forms.ModelChoiceField(label = 'Profesional ', queryset=Profesional.objects.all())
    cliente = forms.ModelChoiceField(label = 'Cliente ', queryset=Cliente.objects.all())
    texto_comentario = forms.CharField(label = 'Comentario ',max_length=400, required=False, widget=forms.Textarea(attrs={}))
    recomendacion = forms.BooleanField(label = 'Recomendarías ', required=False, initial=True)
    valoracion = forms.IntegerField(label = 'Valoración ', required=True, min_value=1, max_value=5, initial=1)