from rest_framework import serializers
from images.models import Images

class ImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = ('id', 'title', 'src', 'description', 'user')