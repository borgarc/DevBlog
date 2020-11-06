from django.shortcuts import render
from images.models import Images
from images.serializers import ImagesSerializer
from rest_framework import viewsets

class ImageView(viewsets.ModelViewSet):
    queryset = Images.objects.all()
    serializer_class = ImagesSerializer
