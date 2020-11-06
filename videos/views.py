from django.shortcuts import render
from videos.models import Video
from videos.serializers import VideoSerializer
from rest_framework import viewsets

class VideoView(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer

