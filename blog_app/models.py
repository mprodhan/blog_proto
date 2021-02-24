from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

class Author(AbstractUser):
    author = models.CharField(max_length=30)

    def __str__(self):
        return self.author

class Blog(models.Model):
    title = models.CharField(max_length=30)
    body = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    author_name = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


