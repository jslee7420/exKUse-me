from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    phone_number=models.CharField(max_length=11)
    major=models.CharField(max_length=100)
    introduction=models.CharField(max_length=100,blank="True")
    online_letter=models.BooleanField()
    is_korean=models.BooleanField()
    is_foreigner=models.BooleanField()

class KoreanUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    LANGUAGE_CHOICES = [
        ('보통화', 'MADARIN CHINESE'),
        ('스페인어', 'SPANISH'),
        ('영어', 'ENGLISH'),
        ('힌디어', 'HINDI'),
        ('뱅골어', 'BENGALI'),
        ('포르투갈어', 'PORTUGUESE'),
        ('러시아어', 'RUSSIAN'),
        ('일본어', 'JAPANESE'),
        ('란다어', 'WESTERN PUNJABI'),
        ('마라티어', 'MARATHI'),
        ('텔루구어', 'TELUGU'),
        ('우어', 'WU CHINESE'),
        ('터키어', 'TURKISH'),
        ('불어', 'FRENCH'),
        ('독어', 'GERMAN'),
        ('베트남어', 'VIETNAMESE'),
        ('타밀어', 'TAMIL'),
        ('웨어', 'YUE CHINESE'),
        ('우르두어', 'URDU'),
        ('자와어', 'JAVANESE'),
    ]
    language = models.CharField(choices=LANGUAGE_CHOICES, blank=True, max_length=100)

    LEVEL_CHOICES=[
        ('상','ADVANCED'),
        ('중','INTERMIDIATE'),
        ('하','BASIC'),
    ]
    language_level=models.CharField(choices=LEVEL_CHOICES, blank=True, max_length=100)




class ForeignUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    country=models.CharField(max_length=100)
    LANGUAGE_CHOICES = [
        ('MADARIN CHINESE', 'MADARIN CHINESE'),
        ('SPANISH', 'SPANISH'),
        ('ENGLISH', 'ENGLISH'),
        ('HINDI', 'HINDI'),
        ('BENGALI', 'BENGALI'),
        ('PORTUGUESE', 'PORTUGUESE'),
        ('RUSSIAN', 'RUSSIAN'),
        ('JAPANESE', 'JAPANESE'),
        ('WESTERN PUNJABI', 'WESTERN PUNJABI'),
        ('MARATHI', 'MARATHI'),
        ('TELUGU', 'TELUGU'),
        ('WU CHINESE', 'WU CHINESE'),
        ('TURKISH', 'TURKISH'),
        ('FRENCH', 'FRENCH'),
        ('GERMAN', 'GERMAN'),
        ('VIETNAMESE', 'VIETNAMESE'),
        ('TAMIL', 'TAMIL'),
        ('YUE CHINESE', 'YUE CHINESE'),
        ('URDU', 'URDU'),
        ('JAVANESE', 'JAVANESE'),
    ]
    native_language=models.CharField(choices=LANGUAGE_CHOICES, max_length=100)

    LEVEL_CHOICES=[
        ('ADVANCED','ADVANCED'),
        ('INTERMIDIATE','INTERMIDIATE'),
        ('BASIC','BASIC'),
    ]
    korean_level=models.CharField(choices=LEVEL_CHOICES, max_length=100)