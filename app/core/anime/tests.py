from django.test import TestCase
from rest_framework.test import RequestsClient,force_authenticate
from django.contrib.auth.models import User
from core.anime.models import Anime
# Create your tests here.

class TestAnimeModel(TestCase):
    def  test_create_anime(self):
        """test create new anime"""
        anime = Anime.objects.create(title="Dragon ball")


        self.assertIsInstance(anime,Anime)

    def test_delete_anime(self):
        """test delete anime"""

        anime = Anime.objects.create(title="Dragon ball")

        anime.objects.delete()

        


class TestAnimeResponse(TestCase):
    """pruebas para el modulo anime"""

    CLIENT = RequestsClient()

    def test_get_response_status_200(self):
        """test response get method"""
        user = User.objects.first()



        request = self.CLIENT.get('http://testserver/animes')
        force_authenticate(request,user=user)


        self.assertEqual(request.status_code,200)

    # def test_get_response_data(self):
    #     """test response get method"""

    #     user = User.objects.first()



    #     request = self.CLIENT.get('http://testserver/animes')
    #     force_authenticate(request,user=user)

    #     self.assertJSONEqual()