from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.
def home(request):
    allPosts = Post.objects.all()
    context = {'allPosts': allPosts}
    return render(request, 'blog/index.html', context)

def blogPost(request, slug):
    post = Post.objects.get(slug=slug)
    context = {'post': post}
    return render(request, 'blog/blogPost.html', context)