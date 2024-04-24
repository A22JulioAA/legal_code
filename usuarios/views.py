from django.shortcuts import render
from .models import Cliente, Especialidad
from django.http import HttpResponse
from .forms import RegistroClienteForm, RegistroProfesionalForm, LoginClienteForm, LoginProfesionalForm

# def crear_especialidad(request):
#     # especialidad = Especialidad(nombre = 'Julio')
#     # especialidad.save()
    
#     especialidad = Especialidad.objects.create(nombre = 'Mercantil')

# def eliminar_especialidad(request):
#     Especialidad.objects.filter(id=1).delete()

# def crear_cliente(request):
#     cliente = Cliente(nombre = 'Julio', apellidos = 'Aller Acuña', email = 'a22julioaa@iessanclemente.net', password = 'abc123.',
#                       fecha_nacimiento = '2002-04-19', telefono = '9987645342')
#     cliente.save()

def registro(request):
    if 1 == 1:
        formulario_registro = RegistroClienteForm()
    else:
        formulario_registro = RegistroProfesionalForm()

    return render(request, 'registro.html', {'formulario_registro': formulario_registro})

def login(request):
    if 1 == 2:
        formulario_login = LoginClienteForm()
    else:
        formulario_login = LoginProfesionalForm()

    return render(request, 'login.html', {'formulario_login': formulario_login})


    
