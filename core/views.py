import json
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, authenticate, login
from .forms import RegistroForm
from .models import Profesional, Especialidad
from citas.models import Cita
from django.http import JsonResponse
from django.contrib import messages
from comentarios.forms import CrearComentarioForm
from django.db.models import Avg
from comentarios.models import Comentario

"""
    Cada función define una vista de la web que luego se le pasarán al archivo urls.py
    para crear las rutas asociadas. 
    En el diccionario 'data' se almacena el contexto del renderizado, es decir, los 
    datos que se le pasan a la plantilla para que esta sea dinámica.

"""

# Vista para la página principal
def homepage(request):
    """
    Esta vista carga la página principal los profesionales de la base de datos organizados en 
    cards. Si se introduce un filtro en la url los profesionales se ordenarán según ese filtro.

    Args:
        request (HTTP): Esta request se refiere a la petición que recibe del servidor.

    Returns:
        django.http.HttpResponse: El render carga una plantilla indicada en el 2 argumento y lo carga 
        junto con el contexto de data.
    """

    # Primero sacamos todas las especialidades para cargarlas en la sección de filtros.
    especialidades = Especialidad.objects.all()
    
    lista_profesionales = Profesional.objects.annotate(media_valoracion=Avg('comentarios__valoracion'))
        
    if request.method == 'POST':
        form_type = request.POST.get('form_type')
        
        if form_type == 'filtro_especialidad':
            especialidad_id = request.POST.get('especialidad')
            if especialidad_id:
                especialidad = Especialidad.objects.get(id=especialidad_id)
            else:
                especialidad = None
            precio_maximo = request.POST.get('precio')

            if especialidad:
                lista_profesionales = especialidad.profesional_set.all().annotate(media_valoracion=Avg('comentarios__valoracion'))
            if precio_maximo:
                lista_profesionales = lista_profesionales.filter(precio_consulta__lte=precio_maximo)
    
    if len(lista_profesionales) == 0:
        no_profesionales_especialidad = 'No se han encontrado profesionales con esta especialidad y precio. Lo sentimos mucho...'
    else:
        no_profesionales_especialidad = ''
            
        
    if request.method == 'POST':
        comment_form = CrearComentarioForm(request.POST)
        
        if form_type == 'comentario': 
            if request.user.is_anonymous:
                messages.error(request, 'Debes iniciar sesión para poder comentar.')
                return redirect('login')
            else:
                if comment_form.is_valid():
                    profesional_id = request.POST.get('profesional_id')
                    profesional = Profesional.objects.get(id=profesional_id)
                    
                    comentario = comment_form.save(commit=False)
                    
                    comentario.profesional = profesional
                    comentario.cliente = request.user
                    
                    comment_form.save()

                    messages.success(request, 'Tu comentario se ha enviado con éxito.')
                    return redirect('homepage')
    else:
        comment_form = CrearComentarioForm()
                
    data = {
        'lista_profesionales': lista_profesionales,
        'no_profesionales_especialidad': no_profesionales_especialidad,
        'especialidades': especialidades,
        'comment_form': comment_form
    }
    
    return render(request, 'core/homepage.html', data)

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
                for field, errors in form.errors.items():
                    for error in errors:
                        messages.error(request, f'No se ha podido registrar el usuario. {error}')          
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
    
    # Cargamos una lista de eventos que mostrar en la página del calendario.
    eventos_legales = [
    {
        'titulo': 'Conferencia sobre Derecho Internacional',
        'descripcion': 'Conferencia anual sobre los últimos desarrollos en derecho internacional.',
        'fecha': '2024-07-15',
        'hora': '09:00',
        'tipo_entrada': 'Libre',
        'ubicacion': 'Centro de Convenciones de la Ciudad',
    },
    {
        'titulo': 'Seminario de Derecho Laboral',
        'descripcion': 'Seminario intensivo sobre los aspectos legales relacionados con el empleo y el trabajo.',
        'fecha': '2024-08-20',
        'hora': '14:00',
        'tipo_entrada': '10€',
        'ubicacion': 'Universidad de la Ciudad',
    },
    {
        'titulo': 'Curso de Propiedad Intelectual',
        'descripcion': 'Curso de tres días sobre leyes y prácticas relacionadas con la propiedad intelectual.',
        'fecha': '2024-09-10',
        'hora': '10:30',
        'tipo_entrada': '45€',
        'ubicacion': 'Colegio de Abogados del Condado',
    },
    {
        'titulo': 'Taller de Mediación Familiar',
        'descripcion': 'Taller práctico sobre mediación familiar y resolución de conflictos.',
        'fecha': '2024-10-05',
        'hora': '16:00',
        'tipo_entrada': 'Libre',
        'ubicacion': 'Centro Comunitario',
    },
    {
        'titulo': 'Conferencia sobre Privacidad en Internet',
        'descripcion': 'Charla informativa sobre la privacidad en línea y la legislación relacionada.',
        'fecha': '2024-11-12',
        'hora': '11:30',
        'tipo_entrada': 'Libre',
        'ubicacion': 'Oficinas de la Asociación de Tecnología',
    },
    {
        'titulo': 'Seminario de Derecho Penal',
        'descripcion': 'Seminario avanzado sobre temas actuales en derecho penal y procedimientos judiciales.',
        'fecha': '2025-01-18',
        'hora': '13:45',
        'tipo_entrada': '10€',
        'ubicacion': 'Tribunal de la Ciudad',
    },
    {
        'titulo': 'Curso de Derecho Ambiental',
        'descripcion': 'Curso introductorio sobre leyes y regulaciones ambientales y su aplicación práctica.',
        'fecha': '2025-02-22',
        'hora': '09:30',
        'tipo_entrada': 'Libre',
        'ubicacion': 'Centro de Recursos Ambientales',
    },
    {
        'titulo': 'Taller de Negociación Legal',
        'descripcion': 'Taller práctico sobre habilidades de negociación para profesionales legales.',
        'fecha': '2025-03-30',
        'hora': '15:15',
        'tipo_entrada': '5€',
        'ubicacion': 'Cámara de Comercio',
    },
    {
        'titulo': 'Conferencia de Derechos Humanos',
        'descripcion': 'Conferencia internacional sobre el estado actual de los derechos humanos en todo el mundo.',
        'fecha': '2025-04-25',
        'hora': '10:00',
        'tipo_entrada': 'Libre',
        'ubicacion': 'Universidad Nacional',
    },
    {
        'titulo': 'Seminario de Derecho de la Salud',
        'descripcion': 'Seminario sobre los desafíos legales y éticos en el campo de la salud y la medicina.',
        'fecha': '2025-05-20',
        'hora': '08:45',
        'tipo_entrada': '12€',
        'ubicacion': 'Hospital Principal de la Ciudad',
    },
]

    return render(request, 'core/calendario.html', {'eventos_legales': eventos_legales})

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

@login_required
def obtener_citas(request):
    '''
    Obtiene las citas del cliente actual.

    Args:
        request (HTTP): La solicitud HTTP recibida.

    Returns:
        Un objeto JsonResponse que contiene las citas del cliente actual.

    '''
    
    citas = list(Cita.objects.filter(cliente_id=request.user.id).values())

    return JsonResponse(citas, safe=False)

@login_required
def anular_cita(request, id_cita):
    """
    Anula una cita existente en el sistema.

    Parameters:
        request (HttpRequest): La solicitud HTTP recibida.
        id_cita (int): El ID de la cita a anular.

    Returns:
        HttpResponseRedirect: Una redirección a la página de inicio.

    """

    if request.method == 'POST':
        cita = Cita.objects.get(id=id_cita)
        cita.delete()
        messages.success(request, 'Tu cita se ha anulado con éxito.')
        return redirect('citas-principal')
    else:
        messages.error(request, 'No se ha podido anular tu cita.')
        return redirect('citas-principal')
    
def politica_cancelaciones(request):
    """
    Vista para la política de cancelaciones.

    Parameters:
        request (HttpRequest): La solicitud HTTP recibida.

    Returns:
        HttpResponse: La respuesta HTTP que se enviará al cliente.

    """
    return render(request, 'core/politica-cancelaciones.html')

