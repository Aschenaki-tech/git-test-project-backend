# serializers.py
from rest_framework import serializers
from .models import Song
from django.contrib.auth.models import User


class SongSerializer(serializers.ModelSerializer):
        
    class Meta:
        model = Song
        fields = '__all__'



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user