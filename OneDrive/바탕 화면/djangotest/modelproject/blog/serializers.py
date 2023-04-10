from rest_framework import serializers
from dataclasses import field
from .models import Blog

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['id', 'user', 'title', 'body']
        read_only_fields = ['user']