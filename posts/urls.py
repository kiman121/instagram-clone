from django.urls import path
from . import views

urlpatterns = [
    path('', views.explore, name='explore'),
    path('timeline', views.timeline, name='timeline'),
    path('upload-photo/', views.uploadPhoto, name='upload-photo'),
    path('post-detail/<str:pk>/', views.postDetail, name='post-detail'),
    path('add-comment/<str:pk>/', views.addComment, name='add-comment'),
    path('add-like/<str:pk>/', views.addLike, name='add-like'),
    path('follow-user/<str:followee_pk>/', views.followUser, name='follow-user'),
    path('un-follow-user/<str:followee_pk>/', views.unFollowUser, name='un-follow-user'),
]