from django.contrib import admin
from .models import Site, Photo, File

for i in [Site, Photo, File]:
    admin.site.register(i)