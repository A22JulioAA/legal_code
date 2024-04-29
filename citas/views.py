from django.shortcuts import render
from .models import Cita

# Create your views here.

def citas_principal(request):
    # Obtenemos todas las citas asociadas al profesional 
    citas = Cita.objects.all()

    data = {
        'citas': citas,
    }

    return render(request, 'citas_principal.html', data)
