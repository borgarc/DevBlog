from django.shortcuts import render
from comments.models import Comments
from comments.serialiozers import CommentsSerializer
from rest_framework import viewsets

class CommentsView(viewsets.ModelViewSet):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer
