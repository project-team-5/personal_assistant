# media_app/views.py
from django.shortcuts import render


def upload_media(request):
    return render(request, 'media_app/upload_media.html')
