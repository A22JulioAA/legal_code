from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from core.forms import ModificarUsuarioForm

@login_required
def profile(request):
    if request.method == 'POST':
        form = ModificarUsuarioForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Redirigir al perfil después de guardar los cambios
    else:
        form = ModificarUsuarioForm(instance=request.user)    
    
    data = {
        'form': form
    }
    
    return render(request, 'profile.html', data)
        

@login_required
def eliminar_perfil(request):
    '''
    Vista para eliminar el perfil de un usuario.

    Esta función elimina el perfil de un usuario. Comprueba si la solicitud es de tipo POST y elimina el usuario si es así. 
    En caso contrario, muestra un mensaje de error y redirige al perfil del usuario.

    Parameters:
    - request: La solicitud HTTP recibida.

    Returns:
    - Una redirección a la página de inicio.

    '''
    if request.method == 'POST':
        user = request.user 
        user.delete()
        messages.success(request, 'Tu usuario se ha eliminado con éxito.')
        return redirect('homepage')
    else:
        messages.error(request, 'No se ha podido eliminar tu usuario.')
        return redirect('profile')



