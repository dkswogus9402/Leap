from django.db import models
from django.contrib.auth.models import AbstractUser
from rest_framework.authtoken.models import Token
from django.conf import settings

# Create your models here.

class User(AbstractUser):
    name = models.CharField(max_length = 20) # 가입자 이름
    tell = models.CharField(max_length = 13) # 전화번호
    email = models.CharField(max_length = 255) # 이메일
    location = models.CharField(max_length = 255) # 회사 위치
    is_company = models.BooleanField(default=False)
    is_jobseeker= models.BooleanField(default=False)
    is_academy= models.BooleanField(default=False)
    