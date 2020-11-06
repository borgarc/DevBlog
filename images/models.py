from django.db import models
from people.models import Person

class Images(models.Model):
    title = models.CharField(max_length=50)
    src = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    user = models.ForeignKey(Person, on_delete=models.CASCADE)
