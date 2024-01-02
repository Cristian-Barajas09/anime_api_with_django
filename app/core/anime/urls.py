from django.urls import path
from .views import UploadImageView

app_name = 'animes'

urlpatterns = [
     path('upload_image/<int:anime_id>/', UploadImageView.as_view(), name='upload_image'),
]
