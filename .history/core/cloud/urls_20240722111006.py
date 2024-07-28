# media_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('upload-media/', views.upload_media, name='upload_media'),
]
