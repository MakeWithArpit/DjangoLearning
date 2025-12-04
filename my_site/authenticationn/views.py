from django.shortcuts import render
from django.http import HttpResponse

def auth_home(request):
    return HttpResponse("Welcome to the authentication home page!")

def auth_login(request):
    return render(request, '1login.html')

