from django.shortcuts import render
from comments.models import Comment
from comments.serialiozers import CommentSerializer
from rest_framework import viewsets

class CommentView(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
