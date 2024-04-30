from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, authenticate, login
from .forms import CustomUserCreationForm
from .models import Profesional

# Cada función define una vista de la web que luego se le pasarán al archivo urls.py
# para crear las rutas asociadas. 
# En el diccionario 'data' se almacena el contexto del renderizado, es decir, los 
# datos que se le pasan a la plantilla para que esta sea dinámica.

# Vista para la página principal
def homepage(request):
    lista_profesionales = Profesional.objects.all()

    data = {
        'lista_profesionales': lista_profesionales,

    }
    
    return render(request, 'core/homepage.html', data)

# TODO:A mejorar el registro e inicio de sesión. Implementar cambio de formulario según sea profesional o cliente.
# TODO:Revisar permisos y crear permisos nuevos.
# TODO: Hay movida porque por defecto Django pilla el username para autenticar y los usuarios no tienen username aquí. Estaría de locos no meterlo en el formulario pero que se les creara automáticamente.

# Vista para ver los profesionales.
# El decorador @login_required hace que sea necesario tener una sesión iniciada para acceder
@login_required
def profesionales(request):
    return render(request, 'core/profesionales.html')

# Vista para la función de salir de la sesión. Redirecciona a la homepage
def salir(request):
    logout(request)
    return redirect('homepage')

# Vista para registrarse
def register(request):
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

# Vista para el calendario
@login_required
def calendario(request):
    return render(request, 'core/calendario.html')

# Vista para el Sobre Nosotros
def sobre_nosotros(request):
    return render(request, 'core/sobre_nosotros.html')

# Vista para las solicitudes
@login_required
def solicitudes(request):

    data = {

    }

    return render(request, 'core/solicitudes.html', data)

