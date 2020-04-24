from django.db import models

# Create your models here.
class ydl(models.Model):
    link=models.CharField(max_length=250)

class videos(models.Model):
    av=models.FileField()