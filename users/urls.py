from django.urls import path
from . import views

urlpatters = [
    path('', views.loginUser, name='login'),
]