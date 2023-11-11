from django.db import models
from django.utils import timezone
from django import forms



class Site(models.Model):
    URL_link = models.URLField()
    name = models.TextField()
    PossibleTags = (
        ("Szkola", "Szkola"),
        ("Osobiste", 'Osobiste'),
        ("Inne", "Inne")
    )

    tag = models.CharField(choices=PossibleTags, default="Szkola", max_length=10)
    
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