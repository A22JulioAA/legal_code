from django.shortcuts import render, redirect
from .models import Cita
from django.contrib.auth.decorators import login_required
from .forms import CitaForm
from django.contrib import messages

# Create your views here.

@login_required
def citas_principal(request):
    """
        Esta función requiere de estar logueado y su función es obtener una 
        lista de las citas del usuario y pasarlas como contexto a la template.
        
        Args:
            request: representa la petición HTTP recibida por el servidor.
    """
    citas = Cita.objects.all()

    data = {
        'citas': citas,
    }

    return render(request, 'citas_principal.html', data)

@login_required
def agendar_cita(request):
    if request.method == 'POST':
        form = CitaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'La cita se ha reservado correctamente. Nos vemos!')
            return redirect('homepage')
    else:
        form = CitaForm()

    data = {
        'form': form
    }

    return render(request, 'agendar_cita.html', data)