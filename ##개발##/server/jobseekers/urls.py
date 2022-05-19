from django.urls import path
from .views import JobseekerRegistrationView

app_name = 'jobseekers'

urlpatterns = [
    path('signup/jobseeker/', JobseekerRegistrationView.as_view()),
    
]