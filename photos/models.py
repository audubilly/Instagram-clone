import os
from pathlib import Path

from cloudinary.models import CloudinaryField
from django.db import models

from instagram_Project.settings import MEDIA_DIR

UPLOAD_DIR = os.path.join(MEDIA_DIR, "photos")


class PhotoModel(models.Model):
    # image = models.ImageField()
    image = CloudinaryField('image', folder=UPLOAD_DIR)
    published_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.image
# Create your models here.
