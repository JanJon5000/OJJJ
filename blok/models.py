from django.db import models
from django.utils import timezone


class Site(models.Model):
    URL_link = models.URLField()
    name = models.TextField()

    def __str__(self):
        return self.name

    def publish(self):
        self.save()

class Tab(models.Model):
    URL_link = models.URLField()
    name = models.TextField()

    def __str__(self):
        return self.name

    def publish(self):
        self.save()