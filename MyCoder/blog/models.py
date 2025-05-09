from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your models here.
class Post(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    content = models.TextField(max_length=100000)
    views = models.IntegerField(default=0)
    author = models.CharField(max_length=30)
    slug = models.CharField(max_length=30)
    timeStamp = models.DateTimeField(blank=True)

    def __str__(self):
        return self.title + ', by -> ' + self.author
    
class BlogComment(models.Model):
    sno = models.AutoField(primary_key=True)
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE) # if post is deleted then also delete the comments
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    timeStamp = models.DateTimeField(default=now)

    def __str__(self):
        return str(self.user)+" -> "+str(self.post)