from django.http import HttpResponse
from django.shortcuts import render
from .models import Product
from math import ceil

# Create your views here.
def index(request):
    products = Product.objects.all()
    n = len(products)
    nSlides = n // 4 + ceil((n/4) - (n//4))
    params = {'product': products, 'range': range(1, nSlides), 'no_of_slides': nSlides} 
    return render(request, 'shop/index.html', params)

def about(request):
    return render(request, 'shop/about.html')

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