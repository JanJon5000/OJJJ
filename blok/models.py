from django.db import models
from django.utils import timezone


class Site(models.Model):
    URL_link = models.URLField()
    name = models.TextField()
    publishedDate = models.DateTimeField(blank=True, null=True)
    publishedDate = timezone.now()

    def __str__(self):
        return self.name

class Photo(models.Model):
    upload = models.ImageField(upload_to="uploads/")
    publishedDate = models.DateTimeField(blank=True, null=True)
    publishedDate = timezone.now()

class File(models.Model):
    upload = models.FileField(upload_to="uploads/")
    publishedDate = models.DateTimeField(blank=True, null=True)
    publishedDate = timezone.now()
