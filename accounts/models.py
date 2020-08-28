from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    country=models.CharField(max_length=100)
    phone_number=models.CharField(max_length=11)
    major=models.CharField(max_length=100)
    introduction=models.CharField(max_length=200,blank=True)
    online_letter=models.BooleanField(default=True)
    profile_picture = models.ImageField(blank=True)



class NativeLanguage(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    language=models.CharField(max_length=100)


class StudyingLanguage(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    language=models.CharField(max_length=100)
    LEVEL_CHOICES=[
        ('BASIC','BASIC'),
        ('INTERMIDIATE','INTERMIDIATE'),
        ('ADVANCED','ADVANCED'),
    ]
    level=models.CharField(choices=LEVEL_CHOICES,default='BASIC', max_length=50)