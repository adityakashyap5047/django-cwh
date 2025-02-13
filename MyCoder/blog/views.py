from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.
def home(request):
    posts = Post.objects.all()
    print(posts)
    return render(request, 'blog/index.html')

def blogPost(request, slug):
    return render(request, 'blog/blogPost.html')

