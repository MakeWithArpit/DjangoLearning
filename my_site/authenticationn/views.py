from django.shortcuts import render
from django.http import HttpResponse


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

def file(request):
    return render(request, "about.html")
