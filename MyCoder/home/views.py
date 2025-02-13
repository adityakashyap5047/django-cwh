from django.shortcuts import render
from django.http import HttpResponse
from home.models import Contact
from blog.models import Post
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, 'home/index.html')

def contact(request):
    if request.method == 'POST':
        messages.success(request, "Your Message received successfully. We will get back to you shortly!!!")
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST['phone']
        content = request.POST['content']
        
        contact = Contact(name = name, email = email, phone = phone, content = content)
        contact.save()
    return render(request, 'home/contact.html')

def about(request):
    return render(request, 'home/about.html')

def search(request):
    search = request.GET.get('search')
    searchPosts = Post.objects.filter(title__icontains=search)
    context = {'searchPosts': searchPosts}
    return render(request, 'home/search.html', context)