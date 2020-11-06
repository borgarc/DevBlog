from django.db import models
from people.models import Person
from posts.models import Post

class Comments(models.Model):
    comment = models.CharField(max_length=1000)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(Person, on_delete=models.CASCADE)
