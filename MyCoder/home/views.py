from django.shortcuts import render
from django.http import HttpResponse
from .models import Contact

# Create your views here.
def home(request):
    return render(request, 'home/index.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST['phone']
        content = request.POST['content']
        
        contact = Contact(name = name, email = email, phone = phone, content = content)
        contact.save()
    return render(request, 'home/contact.html')

def about(request):
    return render(request, 'home/about.html')