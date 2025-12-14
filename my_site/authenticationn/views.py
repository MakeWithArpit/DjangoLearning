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
    print(f"your name is {request.GET.get("naMe")} \nyour email is {request.GET["emaIl"]}\nyour message is {request.GET["messaGe"]}")
    return render(request, "contact.html")

def about(request):
    return render(request, "about.html")

def file(request):
    print(f"first value is {request.GET["value1"]} and second value is {request.GET["value2"]}")
    return render(request, "file.html")
