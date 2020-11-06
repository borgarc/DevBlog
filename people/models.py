from django.db import models

class Person(models.Model):
    class Meta:
        verbose_name_plural = "People"

    name = models.CharField(max_length=30)
    second_name = models.CharField(max_length=30)
    nick = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=20)
    email = models.CharField(max_length=50, unique=True)
    is_admin = models.BooleanField(default=False)
