from django.db import models

# myapp/models.py
from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

class MediaFile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file = CloudinaryField('file')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file.public_id
