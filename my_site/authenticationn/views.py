from django.shortcuts import render
from django.http import HttpResponse

def auth_home(request):
    data = {
        "title" : "Authentication Home",
    }
    return render(request, 'index.html', data)

def auth_login(request):
    return render(request, '1login.html')

