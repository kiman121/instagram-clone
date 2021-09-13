from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User

from posts.forms import PostForm
from posts.models import Post
from .models import Profile, Gender
from .forms import CustomUserCreationForm, ProfileForm
# Create your views here.


def loginUser(request):
    if request.user.is_authenticated:
        return redirect('explore')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'Username does not exist')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('explore')
        else:
            messages.error(request, 'Username or password is incorrect')

    context = {'page': 'login'}
    return render(request, 'users/login_register.html', context)


def logoutUser(request):
    logout(request)
    messages.info(request, 'User was logged out!')
    return redirect('login')


def registerUser(request):
    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            messages.success(request, 'User account was created')

            login(request, user)
            return redirect('explore')
        else:
            messages.error(
                request, 'An error has occured during registration!')

    return render(request, 'users/login_register.html')


@login_required(login_url='login')
def userProfile(request):
    profile = request.user.profile
    context = {
        'profile': profile,
        'uploadForm': PostForm(),
        'posts': Post.objects.filter(user=request.user),
        # 'tags': Post.objects.order_by('tag').distinct('tag')
    }
    return render(request, 'users/profile.html', context)


@login_required(login_url='login')
def editProfile(request):
    profile = request.user.profile
    form = ProfileForm(instance=profile)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        
        if form.is_valid():
            form.save()
            return redirect('profile')

    context = {
        'form': form,
        'profile': profile,
        'uploadForm': PostForm(),
    }
    return render(request, 'users/profile_form.html', context)
