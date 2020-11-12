from django.db import models
from django.contrib.auth.models import User

class Video(models.Model):
    title = models.CharField(max_length=50)
    src = models.FileField(upload_to='videoFiles')
    description = models.CharField(max_length=500)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
