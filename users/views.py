from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
#TODO: Implementar la opción de modificar el perfil.
@login_required
def profile(request):
    data = {
        
    }
    
    return render(request, 'profile.html', data)

# @login_required
# def modificar_perfil(request):
#     if request.method == 'POST':
        

@login_required
def eliminar_perfil(request):
    if request.method == 'POST':
        user = request.user 
        user.delete()
        messages.success(request, 'Tu usuario se ha eliminado con éxito.')
        return redirect('homepage')
    else:
        messages.error(request, 'No se ha podido eliminar tu usuario.')
        return redirect('profile')



