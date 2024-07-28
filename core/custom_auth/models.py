from django.db import models
from django.contrib.auth.models import User
from PIL import Image
import datetime
from io import BytesIO
from django.core.files.base import ContentFile

# Extending User Model Using a One-To-One Link
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(default='core/media/gus.png', upload_to='profile_images')
    # date_birth = models.DateField(default= datetime.date.today()) 
    address= models.CharField(default='my address')
    # email=models.EmailField()
    # phone_number= models.CharField()

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        try:
            if self.avatar:
                # Відкриваємо зображення аватара
                img = Image.open(self.avatar)

                if img.height > 250 or img.width > 250:
                    new_img = img.resize((250, 250), Image.ANTIALIAS)

                    # Зберігаємо зображення у тимчасовий об'єкт BytesIO
                    output = BytesIO()
                    new_img.save(output, format='JPEG')
                    output.seek(0)

                    # Зберігаємо зображення з новим ім'ям
                    self.avatar.save(f"{self.user.username}_avatar.jpg", ContentFile(output.read()), save=False)
                    output.close()
        except Exception as e:
            print(f' It was error is signals: {e}')
        super().save(*args, **kwargs)
    
    # resizing images
    # def save(self, *args, **kwargs):
    #     super().save()

    #     img = Image.open(self.avatar.path)

    #     if img.height > 250 or img.width > 250:
    #         new_img = (250, 250)
    #         img.thumbnail(new_img)
    #         img.save(self.avatar.path)

        
