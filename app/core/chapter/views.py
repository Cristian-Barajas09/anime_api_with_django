"""vistas para el modelo de los capitulos"""
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Chapter
from .serializer import ChapterSerializer, UploadImageSerializer

# Create your views here.

class ChapterViewSet(viewsets.ModelViewSet):
    """vista para el modelo de los capitulos"""
    queryset = Chapter.objects.all()
    serializer_class = ChapterSerializer


class UploadImageViewSet(APIView):
    """subir imagen"""
    serializer_class = UploadImageSerializer

    def put(self, request, *args,**kwargs):
        """subir imagen"""
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
