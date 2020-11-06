from django.db import models
from people.models import Person

class Video(models.Model):
    title = models.CharField(max_length=50)
    src = models.FileField(upload_to='videoFiles')
    description = models.CharField(max_length=500)
    user = models.ForeignKey(Person, on_delete=models.CASCADE)
