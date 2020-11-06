from django.shortcuts import render
from images.models import Image
from images.serializers import ImageSerializer
from rest_framework import viewsets

class ImageView(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
