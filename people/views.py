from django.shortcuts import render
from django.contrib.auth.models import User
from people.serializers import PersonSerializer
from rest_framework import viewsets

class PeopleView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = PersonSerializer

