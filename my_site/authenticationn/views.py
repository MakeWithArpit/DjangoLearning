from django.shortcuts import render
from django.http import HttpResponse

def auth_home(request):
    return render(request, 'index.html')

