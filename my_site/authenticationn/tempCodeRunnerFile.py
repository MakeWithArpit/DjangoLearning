
def file(request):
    print(f"first value is {request.GET["value1"]} and second value is {request.GET["value2"]}")
    return render(request, "file.html")
