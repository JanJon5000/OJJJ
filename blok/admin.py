from django.contrib import admin
from .models import Site, Tab

for i in [Site, Tab]:
    admin.site.register(i)