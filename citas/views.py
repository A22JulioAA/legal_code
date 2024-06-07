from datetime import timedelta
from django.shortcuts import render, redirect
from .models import Cita
from django.contrib.auth.decorators import login_required
from .forms import CitaForm
from django.contrib import messages
from core.models import Profesional
from django.utils import timezone

@login_required
def citas_principal(request):
    """
        Esta función requiere de estar logueado y su función es obtener una 
        lista de las citas del usuario y pasarlas como contexto a la template.
        
        Args:
            request: representa la petición HTTP recibida por el servidor.
    """
    citas = Cita.objects.filter(cliente_id=request.user.id)

    data = {
        'citas': citas,
    }

    return render(request, 'citas_principal.html', data)

@login_required
def agendar_cita(request, id_profesional = None):
    """
        Esta función requiere estar logueado y sirve para agendar una cita con un pro-
        fesional. Dependiendo de si se entra a este formulario a través del link del
        navbar o a través de una card de las ofertas, el campo de profesional estará vacío
        o con el profesional de la card precargado. Comprueba que la fecha esté libre y el 
        profesional también y añade la cita a la base de datos.

        Args:
            request: representa la petición HTTP recibida por el servidor.
            id_profesional: Puede ser None. Representa el ID del profesional para la cita.
        
        Returns:  
            render: Renderizado del HTML que contiene el formulario de Citas.
    """

    if id_profesional:
        # Recuperamos el profesional para agendar la cita.
        profesional = Profesional.objects.filter(id=id_profesional)

    if request.method == 'POST':
        form = CitaForm(request.POST)

        # Esto lo obtenemos para asegurarnos de que esa fecha y ese profesional estén disponibles.
        fecha_cita = request.POST['fecha_cita']
        # profesional = request.POST['profesional']
        profesional = Profesional.objects.get(id = id_profesional)

        cita_existe = Cita.objects.filter(fecha_cita=fecha_cita, profesional=profesional).exists()

        if cita_existe:
            form = CitaForm()
            return render(request, 'agendar_cita.html', {'error': f'{profesional} no tiene esa fecha disponible. Inténtelo con otra!', 'form': form})
        else:
            if form.is_valid():
                # Cuando ponemos commit=False no añadimos la cita a la base de datos, se crea una instancia que 
                # luego modificaremos según los valores que querramos que tenga. 
                cita = form.save(commit=False)
                # Comprobamos la fecha de la cita
                if cita.fecha_cita < timezone.now() + timedelta(days=2):
                    form = CitaForm()
                    return render(request, 'agendar_cita.html', {'error': 'La cita debe pedirse con al menos 2 días de antelación. Pruebe con otra fecha!', 'form': form})
                # Guardamos el id del profesional que tiene la sesión iniciada.
                cita.profesional_id = profesional.id
                # Guardamos el id del cliente que tiene la sesión iniciada.
                cita.cliente = request.user
                # Aquí obtenemos el precio del profesional seleccionado. Cada profesional tiene un precio por
                # consulta preestablecido en su registro de la base de datos. El usuario no puede cambiarlo.
                profesional_cita = profesional
                cita.precio = profesional_cita.precio_consulta
                # Por último, establecemos el estado en PENDIENTE, que significa que se ha aceptado y se espera
                # al día de la cita. Más adelante se puede CANCELAR o poneerla en ESPERA.
                cita.estado = 'P'
                # Guardamos en la base de datos y enviamos un mensaje flash al homepage para 
                # advertir al usuario de que la cita se agendó con éxito.
                form.save()
                messages.success(request, 'La cita se ha reservado correctamente. Nos vemos muy pronto!')
                return redirect('homepage')
    else:
        if id_profesional is not None:
            profesional = Profesional.objects.get(id=id_profesional)
            form = CitaForm(initial={'profesional':profesional})
        else:
            form = CitaForm()

    data = {
        'form': form,
        'profesional': profesional
    }

    return render(request, 'agendar_cita.html', data)
