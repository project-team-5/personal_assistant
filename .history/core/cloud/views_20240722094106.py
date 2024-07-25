# media_app/views.py
from django.shortcuts import render


def upload_media(request):
    return render(request, 'cloud/upload_media.html')
