from django.http import HttpResponse

def about_us(request):
    return HttpResponse("This is the About Us page of the website.")