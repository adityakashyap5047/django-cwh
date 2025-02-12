from django.shortcuts import render
from .models import Blogpost

# Create your views here.
def index(request):
    myposts = Blogpost.objects.all()
    return render(request, 'blog/index.html', {'myposts': myposts})

def blogpost(request, id):
    post = Blogpost.objects.filter(post_id=id)[0]
    # .order_by('-post_id'): This orders the filtered results by post_id in descending order (-post_id).
    previous_post = Blogpost.objects.filter(post_id__lt=id).order_by('-post_id').first()
    next_post = Blogpost.objects.filter(post_id__gt=id).order_by('post_id').first()
    context = {'post': post, 'prev_post': previous_post, 'next_post': next_post}
    return render(request, 'blog/blogpost.html', context)