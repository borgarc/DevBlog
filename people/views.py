from django.shortcuts import render
from people.models import Person
from people.serializers import PersonSerializer
from rest_framework import viewsets

class PeopleView(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

