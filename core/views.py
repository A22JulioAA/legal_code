from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

# Create your views here.

def homepage(request):
    return render(request, 'core/homepage.html')

@login_required
def profesionales(request):
    return render(request, 'core/profesionales.html')

def salir(request):
    logout(request)
    return redirect('homepage')
