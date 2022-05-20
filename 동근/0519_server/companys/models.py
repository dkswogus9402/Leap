from asyncio.windows_events import NULL
from django.db import models
from django.conf import settings

# Company App
class Company(models.Model):
    name = models.CharField(max_length = 20) # 가입자 이름
    tell = models.CharField(max_length = 13) # 전화번호
    email = models.CharField(max_length = 255) # 이메일
    location = models.CharField(max_length = 255) # 회사 위치
    company = models.OneToOneField(
      settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    number_of_workers = models.IntegerField() # 근무자 수
    year_of_establishment = models.IntegerField() # 설립년도
    industry = models.CharField(max_length = 255) # 산업군
    company_size = models.CharField(max_length = 255) # 기업규모

    def __str__(self):
        return self.company.username


class JobPosting(models.Model):
    salary = models.CharField(max_length=255) # 연봉, 협의같은 정보 ChiceFiled로 할지 고민 
    job_position = models.CharField(max_length=255) # 담당업무
    welfare = models.TextField() # 복리후생
    application_process = models.TextField() #지원방법
    registeration = models.DateTimeField() # 공고 등록일
    expired = models.DateTimeField() # 공고 마감일
    preferential_requirements = models.TextField()
    requestments = models.TextField()
    employment_type = models.CharField(max_length=100)# 고용형태
    manager = models.CharField(max_length=100) # 현재 공고의 담당자
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='jobpostings', null=True)
    # progressing Job posting
    # 구인공고와 교육과정 M : N 관계
    application_jobseekers = models.ManyToManyField(settings.JOBSEEKER_MODEL, related_name ='application_postings') 


