from django.http import HttpResponse

def about_us(request):
    return HttpResponse("This is the About Us page of the website.")

def home_page(request):
    return HttpResponse("This is the Home page of the website.")