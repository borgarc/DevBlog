from django.db import models
from django.contrib.auth.models import User
from posts.models import Post

class Comment(models.Model):
    comment = models.CharField(max_length=1000)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
