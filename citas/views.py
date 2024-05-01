from django.shortcuts import render
from .models import Cita
from django.contrib.auth.decorators import login_required


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
