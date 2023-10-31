from django.db import models
from django.utils import timezone


class Site(models.Model):
    # adder = models.TextField()
    # URL_link = models.URLField()
    # name = models.TextField()
    # published_date = models.DateTimeField(blank=True, null=True)
    # published_date = timezone.now()

    # def __str__(self):
    #     return self.name

    def publish(self):
        self.save()

class Photo(models.Model):
    # adder = models.TextField()
    # upload = models.ImageField(upload_to="uploads/")
    # published_date = models.DateTimeField(blank=True, null=True)
    # published_date = timezone.now()

    def publish(self):
        self.save()

class File(models.Model):
    # adder = models.TextField()
    # upload = models.FileField(upload_to="uploads/")
    # published_date = models.DateTimeField(blank=True, null=True)
    # published_date = timezone.now()

    def publish(self):
        self.save()