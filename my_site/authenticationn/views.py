from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'signup.html')

def forgot(request):
    return render(request, 'forgot-password.html')

def contact(request):
    try:
        print(f"name    :    {request.GET['name']}")
        print(f"Email   :    {request.GET['email']}")
        print(f"Message :    {request.GET['message']}")
    except:
        pass    
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')