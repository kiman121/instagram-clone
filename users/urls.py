from django.urls import path
from . import views

urlpatterns = [
    path('', views.loginUser, name='login'),
    path('register/', views.registerUser, name='register'),
    path('logout/', views.logoutUser, name='logout'),
    path('profile/',views.userProfile, name='profile'),
    path('edit-profile/',views.editProfile, name='edit-profile'),
]
