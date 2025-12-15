from django.shortcuts import render,redirect
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
    if request.method == "POST":
        v = int(request.POST.get('value'))
        data['value'] = v
        print(v)
        # result = odd_even_code(v)
        # data['result'] = result
        # redirect('/odd')
    return render(request, "odd.html", data)
