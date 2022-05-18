from django.db import models
from ..companys.models import JobPosting
from ..accounts.models import User
from ..academys.models import Category



class Education(models.Model):
    # direct Education job posting
    # 구인공고와 교육과정 M : N 관계
    job_posting = models.ManyToManyField(JobPosting, on_delete='edu_posting')
    # Progerssing_Education
    # 유저와 교욱과정 M : N 관계 
    # 이수 여부 확인
    progressing_education = models.ManyToManyField(User, related_name='progressing_user')
    # Complete Education
    # 유저와 교욱과정 M : N 관계
    # 이수 완료 여부 확인
    completed_education = models.ManyToManyField(User, related_name='completed_user')
    
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    title = models.CharField(max_length=45)
    content = models.TextField()
    training_period = models.DateTimeField()
    teacher = models.CharField(max_length=45)
    teacher_info = models.TextField()
    location = models.TextField()
    

    def __str__(self):
        return self.title



class Category(models.Model):

    name = models.CharField(max_length=45)

    def __str__(self):
        return self.name

