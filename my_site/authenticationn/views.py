from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to the authentication home page!")

def login(request):
    return render(request, '1login.html')

