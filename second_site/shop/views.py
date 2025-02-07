from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'shop/index.html')

def about(request):
    return HttpResponse("Hello from about")

def contact(request):
    return HttpResponse("Hello from contact")

def tracker(request):
    return HttpResponse("Hello from tracker")

def search(request):
    return HttpResponse("Hello from search")

def prodView(request):
    return HttpResponse("Hello from product view")

def checkOut(request):
    return HttpResponse("Hello from check out")