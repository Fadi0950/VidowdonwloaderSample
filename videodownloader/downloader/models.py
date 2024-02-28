from django.db import models

# Create your models here.

class DownloadedVideo(models.Model):
    title = models.CharField(max_length=200)
    url = models.URLField(max_length=200)
    file_path = models.CharField(max_length=200)
