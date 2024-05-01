from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, authenticate, login
from .forms import CustomUserCreationForm
from .models import Profesional

"""
    Cada función define una vista de la web que luego se le pasarán al archivo urls.py
    para crear las rutas asociadas. 
    En el diccionario 'data' se almacena el contexto del renderizado, es decir, los 
    datos que se le pasan a la plantilla para que esta sea dinámica.

"""


# Vista para la página principal
def homepage(request):
    """
    Args:
        request (HTTP): Esta request se refiere a la petición que recibe del servidor.

    Returns:
        django.http.HttpResponse: El render carga una plantilla indicada en el 2 argumento y lo carga 
        junto con el contexto de data.
    """
    lista_profesionales = Profesional.objects.all()

    data = {
        'lista_profesionales': lista_profesionales,

    }
    
    return render(request, 'core/homepage.html', data)

# TODO:A mejorar el registro e inicio de sesión. Implementar cambio de formulario según sea profesional o cliente.
# TODO:Revisar permisos y crear permisos nuevos.
# TODO: Hay movida porque por defecto Django pilla el username para autenticar y los usuarios no tienen username aquí. Estaría de locos no meterlo en el formulario pero que se les creara automáticamente.


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
    
    data = {
        'form': CustomUserCreationForm
    }

    if request.method == 'POST':
        user_creation_form = CustomUserCreationForm(data=request.POST)

        if user_creation_form.is_valid():
            user_creation_form.save()

            user = authenticate(username=user_creation_form.cleaned_data['username'], password=user_creation_form.cleaned_data['password1'])
            login(request, user)

            return redirect('homepage')

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

