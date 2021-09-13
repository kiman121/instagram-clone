from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import JsonResponse

from users.models import Profile
from .models import Post, Tag
from .forms import PostForm

# Create your views here.


@login_required(login_url='login')
def explore(request):
    profile = request.user.profile
    posts = Post.objects.all()
    context = {
        'profile': profile,
        'posts':posts,
        'uploadForm': PostForm(),
        'tags': Tag.objects.all(),
    }

    return render(request, 'posts/explore.html', context)

@login_required(login_url='login')
def uploadPhoto(request):
    user = request.user
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        upload = form.save(commit=False)
        upload.user = user
        upload.save()

    return redirect(request.META.get('HTTP_REFERER'))

@login_required(login_url='login')
def postDetail(request,pk):
    post = Post.objects.get(id=pk)
    data = {
        'id': post.id,
        'post_image': post.post_image.url,
        'description': post.description,
        'tag': post.tag.name,
        'user_image':post.user.profile.profile_image.url,
        'user_name':post.user.profile.name,
        'description': post.description,
    }
    return JsonResponse(data)