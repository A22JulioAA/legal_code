from django.shortcuts import render, redirect
from .models import Cita
from django.contrib.auth.decorators import login_required
from .forms import CitaForm
from django.contrib import messages
from core.models import Profesional, Cliente, Especialidad

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
def agendar_cita(request, id_profesional = None):
    if request.method == 'POST':
        form = CitaForm(request.POST)

        fecha_cita = request.POST['fecha_cita']
        profesional = request.POST['profesional']

        cita_existe = Cita.objects.filter(fecha_cita=fecha_cita, profesional=profesional).exists()

        if cita_existe:
            form = CitaForm()
            return render(request, 'agendar_cita.html', {'error': f'{profesional} no tiene esa fecha disponible. Inténtelo con otra!', 'form': form})
        else:
            if form.is_valid():
                form.save()
                messages.success(request, 'La cita se ha reservado correctamente. Nos vemos!')
                return redirect('homepage')
    else:
        if id_profesional is not None:
            profesional = Profesional.objects.get(id=id_profesional)
            form = CitaForm(initial={'profesional':profesional})
        else:
            form = CitaForm()

    data = {
        'form': form
    }

    return render(request, 'agendar_cita.html', data)
