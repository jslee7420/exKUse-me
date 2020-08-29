from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .models import FriendshipRequest, Friend


class SignUpForm(UserCreationForm):
    password1 = forms.CharField(
        label='비밀번호',
        widget=forms.PasswordInput(attrs={'class': 'input_box'})
    )
    password2 = forms.CharField(
        label='비밀번호 확인',
        widget=forms.PasswordInput(attrs={'class': 'input_box'})
    )

    class Meta(UserCreationForm.Meta):
        # 커스텀 유저 모델이 아닌 직접 정의한 유저 모델을 사용하므로 get_user_model()을 사용
        model = get_user_model()
        fields = ('profile_picture','country', 'first_name', 'last_name', 'username', 'password1', 'password2', 'email', 'introduction',)
        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'class': 'input_box',
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'class': 'input_box',
                }
            ),
            'username': forms.TextInput(
                attrs={
                    'class': 'input_box',
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'class': 'input_box',
                }
            ),
            'country': forms.TextInput(
                attrs={
                    'class': 'input_box',
                }
            ),
            'introduction': forms.TextInput(
                attrs={
                    'class': 'input_box long_box',
                }
            )
        }
         # 입력 폼 위의 텍스트
        labels = {
            'first_name': '이름',
            'last_name': '성',
            'email': 'KU 웹메일',
            'country': '국적',
            'introduction': '자기소개'
        }
        # 입력 폼 아래 도움말
        help_texts = {
            'username': ''
        }



class LoginForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ['username', 'password']
        widgets = {
            'username': forms.TextInput(
                attrs={
                    'class': 'input_box',
                    'placeholder': '아이디'
                }
            ),
            'password': forms.PasswordInput(
                attrs={
                    'class': 'input_box',
                    'placeholder': '비밀번호'
                }
            )
        }
        # 입력 폼 위의 텍스트
        labels = {
            'username': '',
            'password': ''
        }

        # 입력 폼 아래 도움말
        help_texts = {
            'username': ''
        }


class FriendshipRelationForm(forms.ModelForm):
    class Meta:
        model=FriendshipRequest
        fields=['from_user','to_user']