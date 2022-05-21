from django.urls import path
from .views import JobseekerRegistrationView
from . import views
app_name = 'jobseekers'

urlpatterns = [
    # jobseeker 회원가입
    path('signup/jobseeker/', JobseekerRegistrationView.as_view()),
    
    # jobseeker 프로필
    path('jobseeker/detail/', views.jobseeker_detail),
]