from django.db import models
from django.conf import settings



class Category(models.Model):
    name = models.CharField(max_length=45)
    def __str__(self):
        return self.name
        

class Academy(models.Model):
    
    academy = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length = 20) # 가입자 이름
    tell = models.CharField(max_length = 13) # 전화번호
    email = models.CharField(max_length = 255) # 이메일
    location = models.CharField(max_length = 255) # 회사 위치
    CEO = models.CharField(max_length=100) # CEO 이름
    site = models.CharField(max_length=255) # 홈페이지 주소

    def __str__(self):
        return self.academy.username



class Education(models.Model):
    # direct Education job posting
    # 구인공고와 교육과정 M : N 관계
    job_posting = models.ManyToManyField(settings.JOBPOSTING_MODEL, related_name ='edu_posting')
    # Progerssing_Education
    # 유저와 교욱과정 M : N 관계 
    # 이수 여부 확인
    progressing_user = models.ManyToManyField(settings.JOBSEEKER_MODEL, related_name='progressing_education')
    # Complete Education
    # 유저와 교욱과정 M : N 관계
    # 이수 완료 여부 확인
    completed_user = models.ManyToManyField(settings.JOBSEEKER_MODEL, related_name='completed_education')
    
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    academy = models.ForeignKey(Academy, on_delete=models.CASCADE)

    title = models.CharField(max_length=45)
    content = models.TextField()
    training_period = models.DateTimeField()
    teacher = models.CharField(max_length=45)
    teacher_info = models.TextField()
    location = models.TextField()
    academy = models.ForeignKey("Academy", on_delete=models.CASCADE)
    

    def __str__(self):
        return self.title




