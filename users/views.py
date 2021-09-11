from django.shortcuts import render

# Create your views here.


def loginUser(request):
    page = 'login'
    context = {
        'page': page,
    }
    return render(request, 'users/login_register.html', context)

def registerUser(request):
    return render(request, 'users/login_register.html')