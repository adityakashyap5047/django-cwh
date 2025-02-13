from django.urls import path
from . import views

urlpatterns = [
    # API to post a comment
    path('postComment', views.postComment, name="Post Comment"),

    path('', views.home, name='Home'),
    path('<str:slug>', views.blogPost, name='Blog Post'),

]