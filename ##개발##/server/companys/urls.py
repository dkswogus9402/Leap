from django.urls import path
from .views import CompanyRegistrationView

app_name = 'companys'

urlpatterns = [
    path('signup/company/', CompanyRegistrationView.as_view()),
    
]