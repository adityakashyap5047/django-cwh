from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post, BlogComment
from django.contrib import messages

# Create your views here.
def home(request):
    allPosts = Post.objects.all()
    context = {'allPosts': allPosts}
    return render(request, 'blog/index.html', context)

def blogPost(request, slug):
    post = Post.objects.get(slug=slug)
    comments = Post.objects.filter(post=post)
    context = {'post': post, 'comments': comments}
    return render(request, 'blog/blogPost.html', context)

# APIs
def postComment(request):
    if request.method == 'POST':
        commnet = request.POST.get("comment")
        user = request.user
        postSno = request.POST.get("postSno")
        post = Post.objects.get(sno=postSno)

        comment = BlogComment(commnet=commnet, user=user, post=post)
        commnet.save()

        messages.success(request, "Comment posted successfully")

    return redirect(f'/blog/{post.slug}')