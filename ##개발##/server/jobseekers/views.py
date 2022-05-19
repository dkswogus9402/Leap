from django.shortcuts import render
from rest_auth.registration.views import RegisterView
from .serializers import JobseekerCustomRegistrationSerializer


class JobseekerRegistrationView(RegisterView):
    serializer_class = JobseekerCustomRegistrationSerializer
