from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='Home'),
    path('<str:slug>', views.blogPost, name='Blog Post'),

    path('postComment', views.postComment, name="postComment")
]