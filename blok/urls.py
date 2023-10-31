from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('index', views.index, name='index'),
    path('', views.main, name='main')
]