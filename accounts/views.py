from django.shortcuts import render, get_object_or_404, redirect
from .models import User
from django.contrib.auth import login as django_login
from django.contrib.auth import authenticate
from .forms import SignUpForm, LoginForm


def login(request):
    form = LoginForm(request.POST or None)
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            django_login(request, user)
            # return redirect('photo:list')
        form.add_error(None, "login_failed")
    return render(request, 'accounts/login.html', {'form': form})

def user_list(request):
    """
    파트너 찾기
    """
    users = User.objects.filter(is_superuser=False)
    context = {'users':users}

    return render(request, 'accounts/user_list.html', context)

def user_info(request, id):
    """
    파트너 정보
    """
    user = get_object_or_404(User, id=id)
    context={'user':user}

    return render(request, 'accounts/user_info.html', context)

def select_signup_method(request):
    return render(request, 'accounts/select_signup_method.html')


def signup(request):
    # POST 방식의 요청이라면 form을 post로 초기화하고, 아니면 none으로 초기화
    form = SignUpForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            user = form.save()
            django_login(request, user)
            return redirect('login')
    return render(request, 'accounts/signup.html', {'form': form})
