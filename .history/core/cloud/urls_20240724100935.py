# media_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('upload-media/', views.upload_media, name='upload_media'),
]


urlpatterns = [
    path('upload/', views.upload_file, name='upload_file'),
    path('files/', views.file_list, name='file_list'),
    path('save-file/', views.save_file, name='save_file'),
]