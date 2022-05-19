from django.shortcuts import render
from rest_auth.registration.views import RegisterView
from .serializers import CompanyCustomRegistrationSerializer
    

# Create your views here.
class CompanyRegistrationView(RegisterView):
    serializer_class = CompanyCustomRegistrationSerializer