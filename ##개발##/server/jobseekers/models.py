from django.db import models
from django.conf import settings


class Resume(models.Model):
    age = models.IntegerField()
    career = models.TextField() # 경력사항
    #portfolio = models.  # 포트폴리오 입력받을 수 있도록 설정
    education = models.CharField(max_length=100) # 학력
    # img = models.ImageField() # 본인 이미지
    name = models.CharField(max_length=100) # 이름



# Create your models here.
class Jobseeker(models.Model):
    jobseeker = models.OneToOneField(
      settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    area = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    description = models.TextField()
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name='jobpostings')

    def __str__(self):
        return self.jobseeker.username


