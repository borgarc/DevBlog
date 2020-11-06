from django.db import models
from people.models import Person

class Post(models.Model):
    content = models.CharField(max_length=1000)
    creation_date = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(Person, on_delete=models.CASCADE)

