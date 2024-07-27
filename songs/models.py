# models.py
from django.db import models
from django.contrib.auth.models import User

class Song(models.Model):
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    album = models.CharField(max_length=100)
    release_date = models.DateField()
    language = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
   

    def __str__(self):
        return self.title
