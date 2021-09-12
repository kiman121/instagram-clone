from django.urls import path
from . import views

urlpatterns = [
    path('', views.explore, name='explore'),
    path('login', views.loginUser, name='login'),
    path('register/', views.registerUser, name='register'),
]
