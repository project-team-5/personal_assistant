from django.db import models
from django.contrib.auth.models import User
from PIL import Image
import datetime


# Extending User Model Using a One-To-One Link
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(default='gus.png', upload_to='profile_images')
    # date_birth = models.DateField(default= datetime.date.today()) 
    address= models.CharField(default='my address')
    # email=models.EmailField()
    # phone_number= models.CharField()

    def __str__(self):
        return self.user.username

    # resizing images
    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.avatar.path)

        if img.height > 250 or img.width > 250:
            new_img = (250, 250)
            img.thumbnail(new_img)
            img.save(self.avatar.path)