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
    if len(search) > 75:
        searchPosts = []
    else:
        searchPostsTitle = Post.objects.filter(title__icontains=search)
        searchPostsContent = Post.objects.filter(content__icontains=search)
        searchPosts = searchPostsTitle.union(searchPostsContent)
    if searchPosts.count() == 0:
        messages.error(request, "No Search results find. Please search the relevant tags!")
    context = {'searchPosts': searchPosts, 'search': search}
    return render(request, 'home/search.html', context)