from django.urls import path
from . import views

urlpatterns = [
    path('', views.file_list, name='file_list'),
    path('', views.site_list, name='site_list'),
    path('', views.photo_list, name='photo_list'),
    path('', views.password, name='haslo')
]