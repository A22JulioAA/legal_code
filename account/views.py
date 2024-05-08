from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import SignUpForm, LoginForm
from django.contrib.auth import authenticate, login
from core.models import Profesional, Cliente
from datetime import datetime

# Create your views here.

def index(request):
    return HttpResponse('Hola')

def register_view(request):
    msg = None
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            if form.cleaned_data.get('is_cliente') == True:
                cliente = Cliente(nombre=form.cleaned_data.get('username'), email=form.cleaned_data.get('email'), password=form.cleaned_data.get('password'), fecha_nacimiento=datetime.now())
                cliente.save()
            user = form.save()
            msg = 'user created'
            return redirect('login_view')
        else:
            msg = 'form is not valid'
    else:
        form = SignUpForm()
    return render(request, 'register.html', {'form': form, 'msg': msg})

def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                msg = 'invalid credentials'
        else:
            msg = 'error validation form'
    return render(request, 'login.html', {'form': form, 'msg': msg})

def home(request):
    return render(request, 'homepage.html')
