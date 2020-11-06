from django.db import models
from people.models import Person
from videos.models import Video
from images.models import Images

class Post(models.Model):
    content = models.CharField(max_length=1000)
    creation_date = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(Person, on_delete=models.CASCADE)
    image = models.ForeignKey(Images, null=True, on_delete=models.CASCADE)
    video = models.ForeignKey(Video, null=True, on_delete=models.CASCADE)

