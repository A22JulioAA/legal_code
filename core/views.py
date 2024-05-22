import json
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, authenticate, login
from .forms import RegistroForm
from .models import Profesional, Especialidad
from citas.models import Cita
from django.http import JsonResponse
from django.contrib import messages

"""
    Cada función define una vista de la web que luego se le pasarán al archivo urls.py
    para crear las rutas asociadas. 
    En el diccionario 'data' se almacena el contexto del renderizado, es decir, los 
    datos que se le pasan a la plantilla para que esta sea dinámica.

"""

# Vista para la página principal
def homepage(request, filtro_especialidad=None, filtro_subespecialidad=None):
    """
    Esta vista carga la página principal los profesionales de la base de datos organizados en 
    cards. Si se introduce un filtro en la url los profesionales se ordenarán según ese filtro.

    Args:
        request (HTTP): Esta request se refiere a la petición que recibe del servidor.

    Returns:
        django.http.HttpResponse: El render carga una plantilla indicada en el 2 argumento y lo carga 
        junto con el contexto de data.
    """
    filtro = None

    # Primero sacamos todas las especialidades para cargarlas en la sección de filtros.
    especialidades = Especialidad.objects.all()
    subespecialidades = None

    if filtro_especialidad == None:
        lista_profesionales = Profesional.objects.all()
    else:
        # Se obtiene la especialidad asociada a ese nombre y luego se buscan los profesionales
        # que la tengan en su lista de especialidades
        especialidad = Especialidad.objects.get(id = filtro_especialidad)
        subespecialidades = especialidad.subespecialidades.all()
        filtro = especialidad.nombre

        lista_profesionales = especialidad.profesional_set.all()
    
    if len(lista_profesionales) == 0:
        no_profesionales_especialidad = 'No se han encontrado profesionales con esta especialidad. Lo sentimos mucho...'
    else:
        no_profesionales_especialidad = ''
        
    data = {
        'lista_profesionales': lista_profesionales,
        'no_profesionales_especialidad': no_profesionales_especialidad,
        'especialidades': especialidades,
        'subespecialidades': subespecialidades,
        'filtro': filtro
    }
    
    return render(request, 'core/homepage.html', data)

def salir(request):
    """
    Vista para la función de salir de la sesión. Redirecciona a la homepage
    
    Args:
        request (HTTP): Esta request se refiere a la petición que recibe del servidor.

    Returns:
        django.http.HttpResponse: Redirecciona la página a la homepage
    """
    
    logout(request)
    return redirect('homepage')

def register(request):
    """
    Esta función comprueba si se ha enviado una petición en la vista del registro. Si es así, comprueba si
    los datos introducidos en el formualario son válidos, y si lo son los añade a la base de datos e inicia
    sesión con ese usuario. Luego redirije a la página principal. Si no se ha enviado nada, simplemente carga 
    la plantilla.
    
    Args:
        request (HTTP): Esta request se refiere a la petición que recibe del servidor.

    Returns:
        django.http.HttpResponse: El render carga una plantilla indicada en el 2 argumento y lo carga 
        junto con el contexto de data.
    """
    if request.user.is_anonymous:
        if request.method == 'POST': 
            form = RegistroForm(request.POST)
            if form.is_valid():
                email = form.cleaned_data.get('email')
                password = form.cleaned_data.get('password1')
                form.save()
                new_user = authenticate(email=email, password=password)
                if new_user is not None:
                    login(request, new_user)
                    return redirect(homepage)            
    else:
        return redirect('logout')
    
    form = RegistroForm()
    
    data = {
        'form': form
    }
        
    return render(request, 'registration/register.html', data)

@login_required
def calendario(request):
    """
    Vista para el calendario
    
    Args:
        request (HTTP): Esta request se refiere a la petición que recibe del servidor.

    Returns:
        django.http.HttpResponse: El render carga una plantilla indicada en el 2 argumento y lo carga 
        junto con el contexto de data.
    """

    return render(request, 'core/calendario.html')

def sobre_nosotros(request):
    """
    Vista para el Sobre Nosotros
    
    Args:
        request (HTTP): Esta request se refiere a la petición que recibe del servidor.

    Returns:
        django.http.HttpResponse: El render carga una plantilla indicada en el 2 argumento y lo carga 
        junto con el contexto de data.
    """
    return render(request, 'core/sobre_nosotros.html')

@login_required
def solicitudes(request):
    """
    Vista para las solicitudes    
    
    Args:
        request (HTTP): Esta request se refiere a la petición que recibe del servidor.

    Returns:
        django.http.HttpResponse: El render carga una plantilla indicada en el 2 argumento y lo carga 
        junto con el contexto de data.
    """

    return render(request, 'core/solicitudes.html')

def obtener_citas(request):
    citas = list(Cita.objects.filter(cliente_id=request.user.id).values())

    return JsonResponse(citas, safe=False)

@login_required
def anular_cita(request, id_cita):
    """
    Anula una cita existente en el sistema.

    Parameters:
        request (HttpRequest): La solicitud HTTP recibida.
        id_cita (int): El ID de la cita a anular.

    Returns:
        HttpResponseRedirect: Una redirección a la página de inicio.

    """

    if request.method == 'POST':
        cita = Cita.objects.get(id=id_cita)
        cita.delete()
        messages.success(request, 'Tu cita se ha anulado con éxito.')
        return redirect('citas-principal')
    else:
        messages.error(request, 'No se ha podido anular tu cita.')
        return redirect('citas-principal')
    
def politica_cancelaciones(request):
    return render(request, 'core/politica-cancelaciones.html')

