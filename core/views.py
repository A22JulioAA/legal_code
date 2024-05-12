from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, authenticate, login
from .forms import RegistroForm
from .models import Profesional, Especialidad
from users.models import Cliente

"""
    Cada función define una vista de la web que luego se le pasarán al archivo urls.py
    para crear las rutas asociadas. 
    En el diccionario 'data' se almacena el contexto del renderizado, es decir, los 
    datos que se le pasan a la plantilla para que esta sea dinámica.

"""

# Vista para la página principal
def homepage(request, filtro_especialidad=None):
    """
    Esta vista carga la página principal los profesionales de la base de datos organizados en 
    cards. Si se introduce un filtro en la url los profesionales se ordenarán según ese filtro.

    Args:
        request (HTTP): Esta request se refiere a la petición que recibe del servidor.

    Returns:
        django.http.HttpResponse: El render carga una plantilla indicada en el 2 argumento y lo carga 
        junto con el contexto de data.
    """

    if filtro_especialidad == None:
        lista_profesionales = Profesional.objects.all()
    else:
        # Se obtiene la especialidad asociada a ese nombre y luego se buscan los profesionales
        # que la tengan en su lista de especialidades
        especialidad = Especialidad.objects.get(nombre = filtro_especialidad)

        lista_profesionales = especialidad.profesional_set.all()
    
    if len(lista_profesionales) == 0:
        no_profesionales_especialidad = 'No se han encontrado profesionales con esta especialidad. Lo sentimos mucho...'
    else:
        no_profesionales_especialidad = ''
        
    print(filtro_especialidad)
    data = {
        'lista_profesionales': lista_profesionales,
        'no_profesionales_especialidad': no_profesionales_especialidad
    }
    
    return render(request, 'core/homepage.html', data)

# TODO:A mejorar el registro e inicio de sesión. Implementar cambio de formulario según sea profesional o cliente.
# TODO:Revisar permisos y crear permisos nuevos.

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

