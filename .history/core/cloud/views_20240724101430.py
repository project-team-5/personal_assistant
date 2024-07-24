# media_app/views.py
from django.shortcuts import render


# def upload_media(request):
#     return render(request, 'cloud/upload_media.html')

# myapp/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import MediaFile


# @login_required
def upload_file(request):
    return render(request, 'cloud/upload_file.html')


# @login_required
def file_list(request):
    files = MediaFile.objects.filter(user=request.user)
    return render(request, 'cloud/file_list.html', {'files': files})


@login_required
def save_file(request):
    if request.method == 'POST':
        public_id = request.POST.get('public_id')
        url = request.POST.get('url')
        if public_id and url:
            MediaFile.objects.create(
                user=request.user,
                file=url
            )
        return redirect('file_list')
    return redirect('upload_file')
