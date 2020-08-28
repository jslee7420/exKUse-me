from django.urls import path
from .views import login, user_list, user_info



urlpatterns = [
    path('login/', login, name='login'),
    path('user_list/', user_list,name='user_list'),
    path('user_info/<int:id>', user_info, name='user_info'),
]
