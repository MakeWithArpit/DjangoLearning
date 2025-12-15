from django.shortcuts import render
from django.http import HttpResponse
from .code import *

data = {} 

def home(request):
    return render(request, "index.html")


def login(request):
    return render(request, "login.html")


def register(request):
    return render(request, "signup.html")


def forgot(request):
    return render(request, "forgot-password.html")


def contact(request):
    return render(request, "contact.html")


def about(request):
    return render(request, "about.html")


def odd(request):
    result = odd_even_code(int(request.POST["value"]))
    data['result'] = result
    return render(request, "odd.html", data)
