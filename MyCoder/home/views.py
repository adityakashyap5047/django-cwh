from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("Hello from home app")

def contact(request):
    return HttpResponse("Hello from home contact")

def about(request):
    return HttpResponse("Hello from home about")