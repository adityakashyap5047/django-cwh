# # I have created this file  - Aditya Kumar

from django.http import HttpResponse

# def index(request):
#     return HttpResponse("Hello from 1st site")

# def about(request):
#     return HttpResponse("<h1>Hello from About</h1>")


def index(request):
    return HttpResponse("Home")

def  removepunc(request):
    return HttpResponse("remove punc")

def capfirst(request):
    return HttpResponse("Capatalize first")