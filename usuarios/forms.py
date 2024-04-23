from django import forms

class RegistroForm(forms.Form):
    nombre = forms.CharField(max_length=100, required=True)
    apellidos = forms.CharField(max_length=100)
