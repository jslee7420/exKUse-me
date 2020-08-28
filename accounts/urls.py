from django.urls import path
from .views import login, select_signup_method, signup

urlpatterns = [
    path('login/', login, name='login'),
    path('select_signup_method/', select_signup_method, name='select_signup_method'),
    path('signup/', signup, name='signup'),
]