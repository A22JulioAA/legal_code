from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, authenticate, login
from .forms import CustomUserCreationForm

# Create your views here.

def homepage(request):
    return render(request, 'core/homepage.html')

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
