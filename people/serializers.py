from rest_framework import serializers
from django.contrib.auth.models import User

class PersonSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        user = User(email=validated_data['email'], username=validated_data['username'], first_name=validated_data['first_name'], last_name=validated_data['last_name'])
        user.set_password(validated_data['password'])
        user.save()
        return user
        
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'username', 'password', 'email', 'is_superuser', 'is_active')

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'is_superuser')