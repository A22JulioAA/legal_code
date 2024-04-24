from django.shortcuts import render
from usuarios.models import Profesional, Especialidad

def homepage(request):
    lista_especialidades = Especialidad.objects.all()
    lista_profesionales = Profesional.objects.all()
    
    return render(request, 'homepage.html', {'lista_especialidades': lista_especialidades, 'lista_profesionales': lista_profesionales})     