from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("from blog app Home")

def blogPost(request, slug):
    return HttpResponse(f"Blog and {slug}")