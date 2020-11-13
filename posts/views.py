from django.shortcuts import render
from posts.models import Post
from posts.serializers import PostSerializer
from devblogback.views import GetUserForPostView
from rest_framework.response import Response

class PostView(GetUserForPostView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    