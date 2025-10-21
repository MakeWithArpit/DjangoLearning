from django.http import HttpResponse
from django.shortcuts import render

def home_page(request):
    data = {
        "title": "Home Page",
        "welcome_message": "Welcome to our website!",
        
        "languages": ["Python", "JavaScript", "Java", "C++", "Ruby"],
        "Students_details": [
            {"name": "Alice", "age": 20, "city": "New York"},
            {"name": "Bob", "age": 22, "city": "Los Angeles"},
            {"name": "Charlie", "age": 23, "city": "Chicago"},
        ]
    }
    return render(request,"index.html", data)

def about_us(request):
    return HttpResponse("This is the About Us page of the website.")

def in_about_us(request,num):
    if num == 1:
        return HttpResponse("This is the first page in About Us page of the website.")
    elif num == 2:
        return HttpResponse("This is the second page in About Us page of the website.")
    else:
        return HttpResponse("This is the About_Us page of the website.")