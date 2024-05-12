from django.shortcuts import render, redirect
from django.http import HttpResponse

def profile(request):
    data = {
        
    }
    
    return render(request, 'profile.html', data)



