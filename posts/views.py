from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User

from users.models import Profile

# Create your views here.


@login_required(login_url='login')
def explore(request):
    profile = request.user.profile

    context = {'profile': profile}

    return render(request, 'posts/explore.html', context)

