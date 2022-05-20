from django.shortcuts import get_object_or_404
from rest_auth.registration.views import RegisterView
from rest_framework.response import Response
from .serializers import JobseekerCustomRegistrationSerializer, JobseekerSerializer
from .models import Jobseeker
from rest_framework.decorators import api_view


class JobseekerRegistrationView(RegisterView):
    serializer_class = JobseekerCustomRegistrationSerializer


@api_view(['GET'])
def jobseeker_detail(request):
    jobseeker = get_object_or_404(Jobseeker, jobseeker_id = request.user.id)
    serializer = JobseekerSerializer(jobseeker)
    return Response(serializer.data)