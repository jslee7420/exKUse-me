from django.db import models
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(max_length=254)
    country = models.CharField(max_length=100)
    # phone_number = models.CharField(max_length=11) 삭제
    major = models.CharField(max_length=100)
    introduction = models.CharField(max_length=200, blank=True)
    # online_letter = models.BooleanField(default=True) 삭제
    profile_picture = models.ImageField(blank=True, upload_to='media/')


class NativeLanguage(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE, related_name="native_language")
    language=models.CharField(max_length=100)

class StudyingLanguage(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE, related_name="studying_language")
    language=models.CharField(max_length=100)
    LEVEL_CHOICES=[
        ('BASIC','BASIC'),
        ('INTERMIDIATE','INTERMIDIATE'),
        ('ADVANCED','ADVANCED'),
    ]
    level=models.CharField(choices=LEVEL_CHOICES,default='BASIC', max_length=50)


class FriendshipRequest(models.Model):
    """ Model to represent friendship requests """
    from_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='friendship_requests_sent')
    to_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='friendship_requests_received')

class Friend(models.Model):
    """ Model to represent Friendships """
    to_user = models.ForeignKey(User, models.CASCADE, related_name='friends')
    from_user = models.ForeignKey(User, models.CASCADE, related_name='_unused_friend_relation')
