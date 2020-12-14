from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.response import Response
from people.serializers import PersonSerializer, ProfileSerializer
from rest_framework import viewsets

class PeopleView(viewsets.ModelViewSet):
    authentication_classes = []
    permission_classes = []

    queryset = User.objects.all()
    serializer_class = PersonSerializer

class ProfileView(viewsets.GenericViewSet):
    serializer_class = ProfileSerializer
    def list(self, request, *args, **kwargs):
        serializer = self.get_serializer(request.user)
        return Response(serializer.data)