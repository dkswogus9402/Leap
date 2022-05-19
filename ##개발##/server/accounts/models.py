from django.db import models
from django.contrib.auth.models import AbstractUser
from rest_framework.authtoken.models import Token
from django.conf import settings

# Create your models here.

class User(AbstractUser):
    is_company = models.BooleanField(default=False)
    is_jobseeker= models.BooleanField(default=False)
    is_academy= models.BooleanField(default=False)
    