from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=30)
    second_name = models.CharField(max_length=30)
    nick = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    is_admin = models.BooleanField(default=False)
