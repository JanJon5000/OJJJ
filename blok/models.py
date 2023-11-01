from django.db import models
from django.utils import timezone


class Site(models.Model):
    URL_link = models.URLField()
    name = models.TextField()

    def __str__(self):
        return self.name

    def publish(self):
        self.save()

class Photo(models.Model):
    upload = models.ImageField(upload_to="uploads/")
    def publish(self):
        self.save()

class File(models.Model):
    name = models.TextField()
    upload = models.FileField(upload_to="uploads/")

    def publish(self):
        self.save()