from django.shortcuts import render
from rest_auth.registration.views import RegisterView
from .serializers import AcademyCustomRegistrationSerializer


class AcademyRegistrationView(RegisterView):
    serializer_class = AcademyCustomRegistrationSerializer
