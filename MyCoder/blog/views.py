from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post, BlogComment
from django.contrib import messages
from blog.templatetags import extras

# Create your views here.
def home(request):
    allPosts = Post.objects.all()
    context = {'allPosts': allPosts}
    return render(request, 'blog/index.html', context)

def blogPost(request, slug):
    post = Post.objects.get(slug=slug)
    comments = BlogComment.objects.filter(post=post, parent=None)
    replies = BlogComment.objects.filter(post=post).exclude(parent=None)
    repDict = {}
    for reply in replies:
        if reply.parent.sno not in repDict.keys():
            repDict[reply.parent.sno] = [reply]
        else:
            repDict[reply.parent.sno].append(reply)
    context = {'post': post, 'comments': comments, 'user': request.user, 'replyDict': repDict}
    return render(request, 'blog/blogPost.html', context)

# APIs
def postComment(request):
    if request.method == 'POST':
        comment = request.POST.get("comment")
        user = request.user
        postSno = request.POST.get("postSno")
        parentSno = request.POST.get("parentSno")
        post = Post.objects.get(sno=postSno)

        if parentSno == "":
            comment = BlogComment(comment=comment, user=user, post=post)
            comment.save()
            messages.success(request, "Comment posted successfully")
        else:
            parent = BlogComment.objects.get(sno=parentSno)
            comment = BlogComment(comment=comment, user=user, post=post, parent=parent)
            comment.save()
            messages.success(request, "Reply posted successfully")

    return redirect(f'/blog/{post.slug}')