from django.http import HttpResponse

def home_page(request):
    return HttpResponse("This is the Home page of the website.")

def about_us(request):
    return HttpResponse("This is the About Us page of the website.")

def in_about_us(request,num):
    if num == 1:
        return HttpResponse("This is the first page in About Us page of the website.")
    elif num == 2:
        return HttpResponse("This is the second page in About Us page of the website.")
    else:
        return HttpResponse("This is the About_Us page of the website.")