from django.shortcuts import render
from django.http import HttpResponse

def auth_home(request):
    # data = {
    #     "title" : "Authentication Home",
        
    #     "course_list" : ["Django", "Flask", "FastAPI", "Tornado"],

    #     "student_list" : [
    #         {"name": "Alice", "age": 24},
    #         {"name": "Bob", "age": 22},
    #         {"name": "Charlie", "age": 23},
    #     ],

    # }
    return render(request, 'home/index.html')

def auth_login(request):
    return render(request, 'authentication/login_page/login.html')

