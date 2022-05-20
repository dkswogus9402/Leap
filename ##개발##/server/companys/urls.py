from django.urls import path
from . import views
from .views import CompanyRegistrationView

app_name = 'companys'

urlpatterns = [
    path('signup/company/', CompanyRegistrationView.as_view()),
    # jobPosting 조회 및 생성
    path('joblist/', views.job_list_or_create),
    # jobPosting detail, update, delete
    path('joblist/<int:jobposting_pk>/', views.job_detail_or_update_or_delete),
    
]