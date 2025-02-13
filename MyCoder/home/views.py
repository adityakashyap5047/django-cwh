from django.shortcuts import render, redirect
from django.http import HttpResponse
from home.models import Contact
from blog.models import Post
from django.contrib import messages
from django.contrib.auth.models import User

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
        searchPosts = Post.objects.none()
    else:
        searchPostsTitle = Post.objects.filter(title__icontains=search)
        searchPostsContent = Post.objects.filter(content__icontains=search)
        searchPosts = searchPostsTitle.union(searchPostsContent)
    if searchPosts.count() == 0:
        messages.warning(request, "No Search results find. Please search the relevant tags!")
    context = {'searchPosts': searchPosts, 'search': search}
    return render(request, 'home/search.html', context)

def handleSignup(request):
    if request.method == 'POST':
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        cnfPass = request.POST['cnfPass']

        # Checks for errorneous inputs
        if (len(username) > 15):
            messages.error(request, "Username must be under 15 character")
            return redirect('/')
        if (not username.isalnum()):
            messages.error(request, "Username should only contains letters and numbers")
            return redirect('/')
        if (pass1 != cnfPass):
            messages.error(request, "Passwords do not matches")
            return redirect('/')

        # create the user
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()

        messages.success(request, "Your account has been successfully created")

        return redirect('/')
    else:
        return HttpResponse('404 - Not Found')