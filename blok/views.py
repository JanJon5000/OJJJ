from django.shortcuts import render
from django.utils import timezone
from .models import Site, File, Photo
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.http import HttpResponse

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                response = HttpResponse(render(request, 'blok/index.html'))
                response['Cache-Control'] = 'no-cache'
                return response
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('blok/login.html')

@login_required
def index(request):
    photos = Photo.objects.all()
    sites = Site.objects.all()
    files = File.objects.all()
    return render(request, 'blok/index.html', {'photos':photos, 'files':files, 'sites':sites})

def main(request):
    if auth.get_user(request).is_authenticated:
        return redirect('index')
    else:
        return redirect('login')
    