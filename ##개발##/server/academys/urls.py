from django.urls import path
from .views import AcademyRegistrationView

app_name = 'academys'

urlpatterns = [
    path('signup/academy/', AcademyRegistrationView.as_view()),
]