import os
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from PIL import Image

class Author(AbstractUser):
    author = models.CharField(max_length=30)

    def __str__(self):
        return self.author

class Blog(models.Model):
    title = models.CharField(max_length=30)
    body = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to='mediafiles/')
    author_name = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        upload_img = Image.open(self.image.path)
        if upload_img.height > 300 or upload_img > 300:
            output_size = (300,300)
            upload_img.thumbnail(output_size)
            upload_img.save(self.image.path)

