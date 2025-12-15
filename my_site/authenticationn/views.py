from django.shortcuts import render
from django.http import HttpResponse
from .code import *

def home(request):
    a()  # Call function a from code.py
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
