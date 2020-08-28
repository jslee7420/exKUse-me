from django.shortcuts import render, get_object_or_404
from .models import User

def login(request):
    return render(request, 'accounts/login.html')

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