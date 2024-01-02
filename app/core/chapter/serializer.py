from dataclasses import dataclass
from rest_framework import serializers
from .models import Chapter

class ChapterSerializer(serializers.ModelSerializer):
    """serializador para el modelo de los capitulos"""
    @dataclass
    class Meta:
        """informacion de la respuesta"""
        model = Chapter
        fields = '__all__'


class UploadImageSerializer(serializers.ModelSerializer):
    """serializador para subir imagenes"""
    @dataclass
    class Meta:
        """informacion de la respuesta"""
        model = Chapter
        fields = ('picture',)
