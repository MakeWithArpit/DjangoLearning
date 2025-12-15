def odd_even_code():
    value = int(request.POST["value"])
    if value % 2 == 0:
        return "Even"
    else:
        return "Odd"
