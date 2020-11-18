from django.shortcuts import render
from posts.models import Post
from posts.serializers import PostSerializer
from devblogback.views import GetUserForPostView
from rest_framework.response import Response
from rest_framework.permissions import BasePermission, IsAuthenticated, SAFE_METHODS

class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS

class PostView(GetUserForPostView):
    permission_classes = [IsAuthenticated|ReadOnly]

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    