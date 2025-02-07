from django.http import HttpResponse
from django.shortcuts import render
from .models import Product

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
    proudcts = Product.objects.all()  # Get all records
    return render(request, 'shop/product.html', {'products': proudcts})

def checkOut(request):
    return HttpResponse("Hello from check out")