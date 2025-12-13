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
    if request.method == "GET":
        name = request.GET.get("name")
        email = request.GET.get("email")
        message = request.GET.get("message")

        if name and email and message:
            print("Name    :", name)
            print("Email   :", email)
            print("Message :", message)
        print("Contact form submitted.")
    return render(request, "contact.html")


def about(request):
    return render(request, "about.html")
