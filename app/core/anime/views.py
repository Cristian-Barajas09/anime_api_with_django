"""controllers for response"""
from rest_framework import viewsets
from rest_framework import views
from rest_framework.response import Response
from rest_framework import status
from .serializers import AnimeSerializer,UploadImageSerializer
from .models import Anime
# Create your views here.

class AnimeViewSet(viewsets.ModelViewSet):
    """query for response"""
    serializer_class = AnimeSerializer
    queryset = Anime.objects.all()


class UploadImageView(views.APIView):
    """upload image for anime"""
    queryset = Anime.objects.all()

    def put(self,request,*args,**kwargs):
        anime_id = kwargs.get('anime_id')
        anime = Anime.objects.get(id=anime_id)
        serializer = UploadImageSerializer(anime, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# def upload_image(request):
#     """save images for anime"""

#     data = request.data

#     anime_id = data['anime_id']
#     obj = Anime.objects.get(id=anime_id)

#     obj.picture = request.FILES.get('image')
#     obj.save()

#     return Response('Image was uploaded')
