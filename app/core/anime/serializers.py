"""serializers for anime app"""
import dataclasses
from rest_framework import serializers
from .models import Anime

class AnimeSerializer(serializers.ModelSerializer):
    """response anime data"""
    @dataclasses.dataclass
    class Meta:
        """information for anime serializers"""
        model = Anime
        fields = [
            'id',
            'title',
            'description',
            'picture'
        ]

class UploadImageSerializer(serializers.ModelSerializer):
    """response for image"""
    @dataclasses.dataclass
    class Meta:
        """info for response"""
        model = Anime
        fields = ['picture']
