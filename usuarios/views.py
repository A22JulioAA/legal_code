from django.shortcuts import render
from .models import Cliente, Especialidad

def crear_especialidad(request):
    # especialidad = Especialidad(nombre = 'Julio')
    # especialidad.save()
    
    especialidad = Especialidad.objects.create(nombre = 'Administrativo')

def eliminar_especialidad(request):
    Especialidad.objects.filter(id=1).delete()

def crear_cliente(request):
    cliente = Cliente(nombre = 'Julio', apellidos = 'Aller Acuña', email = 'a22julioaa@iessanclemente.net', password = 'abc123.',
                      fecha_nacimiento = '2002-04-19', telefono = '9987645342')
    cliente.save()
    
