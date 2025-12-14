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
    data = {"name": "", 
            "email": "", 
            "message": ""
            }

    try:
        name = request.POST["naMe"]
        email = request.POST["emaIl"]
        message = request.POST["messaGe"]

        data["name"] = name
        data["email"] = email   
        data["message"] = message
    except:
        pass

    return render(request, "contact.html", data)


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
