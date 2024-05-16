from rest_framework import serializers
from .models import About, Collaborate

class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = ['id', 'title', 'content', 'last_updated']

class CollaborateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collaborate
        fields = ['id', 'name', 'email', 'message', 'created_at']
