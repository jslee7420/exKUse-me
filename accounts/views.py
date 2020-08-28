from django.shortcuts import render, redirect
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