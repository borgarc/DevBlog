from django.db import models
from django.contrib.auth.models import User
from videos.models import Video
from images.models import Image

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=1000)
    creation_date = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ForeignKey(Image, null=True, on_delete=models.CASCADE)
    video = models.ForeignKey(Video, null=True, on_delete=models.CASCADE)

