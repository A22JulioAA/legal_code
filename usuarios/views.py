from django.shortcuts import render
from .models import Cliente, Especialidad
from django.http import HttpResponse
from .forms import RegistroClienteForm, RegistroProfesionalForm

def crear_especialidad(request):
    # especialidad = Especialidad(nombre = 'Julio')
    # especialidad.save()
    
    especialidad = Especialidad.objects.create(nombre = 'Mercantil')

def eliminar_especialidad(request):
    Especialidad.objects.filter(id=1).delete()

def crear_cliente(request):
    cliente = Cliente(nombre = 'Julio', apellidos = 'Aller Acuña', email = 'a22julioaa@iessanclemente.net', password = 'abc123.',
                      fecha_nacimiento = '2002-04-19', telefono = '9987645342')
    cliente.save()

def registro_cliente(request):
    registro_cliente_form = RegistroClienteForm()
    registro_profesional_form = RegistroProfesionalForm()

    return render(request, 'registro.html', {'registro_cliente_form': registro_cliente_form, 'registro_profesional_form': registro_profesional_form})


    
