from django.urls import path
from . import views

urlpatterns = [
    path('', views.explore, name='explore'),
    path('upload-photo/', views.uploadPhoto, name='upload-photo'),
    # path('post-detail/<str:pk>/', views.postDetail, name='post-detail'),
    path('post-detail/<str:pk>/', views.postDetail, name='post-detail'),
]