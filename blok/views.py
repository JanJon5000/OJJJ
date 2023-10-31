from django.shortcuts import render
from django.utils import timezone
from .models import Site, File, Photo
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return render(request, 'blok/index.html')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('blok/login.html')

def index(request):
    photos = Photo.objects
    sites = Site.objects
    files = File.objects
    
    return render(request, 'blok/index.html', {})

def main(request):
    return redirect('login')