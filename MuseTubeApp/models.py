from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from pytube import YouTube

class Song(models.Model):
    id = models.IntegerField(primary_key=True)
    url = models.CharField(max_length=512, default="")
    title = models.CharField(max_length=512, default="")
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    @classmethod
    def create(cls, url, user):
        yt = YouTube(url)
        title = yt.title
        url = yt.streams.filter(only_audio=True).order_by('abr').desc().first().url
        s = cls(url=url, title=title, user=user)
        s.save()
        # do something with the book
        return s
