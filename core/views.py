from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, authenticate, login
from .forms import CustomUserCreationForm
from .models import Profesional
from comentarios.models import Comentario

# Create your views here.

def homepage(request):
    lista_profesionales = Profesional.objects.all()

    data = {
        'lista_profesionales': lista_profesionales,

    }
    
    return render(request, 'core/homepage.html', data)

# TODO:A mejorar el registro e inicio de sesión. Implementar cambio de formulario según sea profesional o cliente.
# TODO:Revisar permisos y crear permisos nuevos.
# TODO: Hay movida porque por defecto Django pilla el username para autenticar y los usuarios no tienen username aquí. Estaría de locos no meterlo en el formulario pero que se les creara automáticamente.


@login_required
def profesionales(request):
    return render(request, 'core/profesionales.html')

def salir(request):
    logout(request)
    return redirect('homepage')

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

def sobre_nosotros(request):
    return render(request, 'core/sobre_nosotros.html')
