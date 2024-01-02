from django.urls import path

from . import views

app_name = 'chapter'

urlpatterns = [
    path('upload-image/', views.UploadImageViewSet.as_view(), name='upload-image'),
]
