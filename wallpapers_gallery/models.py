from django.db import models

class Wallpaper(models.Model):
    title = models.CharField(max_length=100)
    url = models.URLField()