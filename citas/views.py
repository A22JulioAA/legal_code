from django.shortcuts import render
from .models import Cita
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required
def citas_principal(request):
    # Obtenemos todas las citas asociadas al profesional 
    citas = Cita.objects.all()

    data = {
        'citas': citas,
    }

    return render(request, 'citas_principal.html', data)
