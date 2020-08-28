from django.urls import path
from .views import login, user_list, user_info, select_signup_method, signup



urlpatterns = [
    path('login/', login, name='login'),
    path('user_list/', user_list,name='user_list'),
    path('user_info/<int:id>', user_info, name='user_info'),
    path('select_signup_method/', select_signup_method, name='select_signup_method'),
    path('signup/', signup, name='signup'),
]
