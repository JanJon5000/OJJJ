from django.shortcuts import render
from django.utils import timezone
from .models import Password, Site, File, Photo

def file_list(request):
    files = File.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blok/file_list.html', {})

def site_list(request):
    #sites = Site.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blok/site_list.html', {})

def photo_list(request):
    #photos = Photo.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blok/photo_list.html', {})

def password(request):
    return render(request, 'blok/haslo.html', {})