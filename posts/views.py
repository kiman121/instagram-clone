from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import JsonResponse

from users.models import Profile
from .models import Post, Tag, Comment, Like, Follow
from .forms import PostForm, CommentForm, LikeForm
from .serializer import CommentSerializer
from .utils import fetchComments
# Create your views here.


@login_required(login_url='login')
def timeline(request):
    profile = request.user.profile
    posts = []
    to_follow = []
    
    # Get posts for users that are being followed
    for user in Follow.objects.filter(follower=request.user):
        for post in Post.objects.filter(user=user.followee):
            posts.append(post)

    # Posts for the logged-in user
    for post in Post.objects.all():
        if post.user == request.user:
            posts.append(post)
    
    # Get users to follow
    for user in User.objects.all():
        if Follow.objects.filter(followee=user, follower=request.user).count() == 0 and user != request.user:
            to_follow.append(user)


    context = {
        'profile': profile,
        'posts': posts,
        'uploadForm': PostForm(),
        'commentForm': CommentForm(),
        'to_follow': to_follow,
        'user_followers_count': Follow.objects.filter(followee=request.user).count(),
        'user_following_count': Follow.objects.filter(follower=request.user).count(),
    }
    return render(request, 'posts/timeline.html', context)


@login_required(login_url='login')
def explore(request):
    profile = request.user.profile
    posts = Post.objects.all()
    context = {
        'profile': profile,
        'posts': posts,
        'uploadForm': PostForm(),
        'tags': Tag.objects.all(),
        'commentForm': CommentForm(),
        'user_followers_count': Follow.objects.filter(followee=request.user).count(),
        'user_following_count': Follow.objects.filter(follower=request.user).count(),
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
def postDetail(request, pk):
    post = Post.objects.get(id=pk)
    data = {
        'id': post.id,
        'post_image': post.post_image.url,
        'description': post.description,
        'tag': post.tag.name,
        'user_image': post.user.profile.profile_image.url,
        'user_name': post.user.profile.name,
        'description': post.description,
        'comments': fetchComments(request, post)
    }
    return JsonResponse(data)


@login_required(login_url='login')
def addComment(request, pk):
    if request.method == 'POST':
        post = Post.objects.get(id=pk)
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.user = request.user
            comment.save()

    return redirect(request.META.get('HTTP_REFERER'))


@login_required(login_url='login')
def addLike(request, pk):
    post = Post.objects.get(id=pk)
    user = request.user
    data = {'status': False}

    if Like.objects.filter(post=post, user=user).count() == 0:
        like = Like(user=user, post=post)
        like.save()
        data['status'] = True

        likes = Like.objects.filter(post=post)
        data['num_likes'] = len(likes)

    return redirect(request.META.get('HTTP_REFERER'))


@login_required(login_url='login')
def followUser(request, followee_pk):
    follower = request.user
    followee = User.objects.get(id=followee_pk)
    
    if Follow.objects.filter(followee=followee, follower=follower).count() == 0:
        new_follow = Follow(followee=followee, follower=follower)
        new_follow.save()

    return redirect(request.META.get('HTTP_REFERER'))

@login_required(login_url='login')
def unFollowUser(request, followee_pk):
    follower = request.user
    followee = User.objects.get(id=followee_pk)
    
    Follow.objects.filter(followee=followee, follower=follower).delete()

    return redirect(request.META.get('HTTP_REFERER'))