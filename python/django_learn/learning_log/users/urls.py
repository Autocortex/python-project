"""Определяет схемы URL для пользователей."""
from django.contrib.auth.views import LogoutView
from django.urls import path, include

from . import views

app_name = 'users'
urlpatterns = [
    #Включить URL авторизации по умолчанию.
    path('logout/', LogoutView.as_view(), name='logout'),
    path('', include('django.contrib.auth.urls')),
    path('register/', views.register, name='register')
]