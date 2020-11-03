from django.shortcuts import render
from posts.models import Post
from posts.serializers import PostSerializer
from rest_framework import viewsets

class PostView(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
