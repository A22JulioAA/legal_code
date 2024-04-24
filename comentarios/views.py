from django.shortcuts import render
from .forms import CrearComentarioForm

def crearComentario(request):
    crear_comentario_form = CrearComentarioForm()

    return render(request, 'crear_comentario.html', {'crear_comentario_form': crear_comentario_form})
