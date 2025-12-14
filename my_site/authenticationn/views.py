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
    try:
        name = request.POST["val1"]
        email = request.POST["val2"]
        message = request.POST["val3"]

        print(f"Your name is {name}")
        print(f"Your email is {email}")
        print(f"Your message is {message}")
    except:
        pass

    return render(request, "contact.html")


def about(request):
    return render(request, "about.html")

def file(request):
    try:
        value1 = request.POST["value1"]
        value2 = request.POST["value2"]
        print(f"Value 1: {value1}, Value 2: {value2}")
    except:
        pass
    return render(request, "file.html")
