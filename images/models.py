from django.db import models
from people.models import Person

class Image(models.Model):
    title = models.CharField(max_length=50)
    src = models.FileField(upload_to='imageFiles')
    description = models.CharField(max_length=500)
    user = models.ForeignKey(Person, on_delete=models.CASCADE)
