from django.shortcuts import get_object_or_404

from rest_auth.registration.views import RegisterView
from .serializers import CompanyCustomRegistrationSerializer, CompanySerializer

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import JobPosting, Company
from .serializers import JobPostingListSerializer, JobPostingSerializer

# Create your views here.
class CompanyRegistrationView(RegisterView):
    serializer_class = CompanyCustomRegistrationSerializer


# 전체 조회 및 생성
@api_view(['GET', 'POST'])
def job_list_or_create(request):
    company_info = get_object_or_404(Company, company_id=request.user.id)

    def job_list():
        # comment 개수 추가
        jobpostings = JobPosting.objects.order_by('-pk')
        serializer = JobPostingListSerializer(jobpostings, many=True)
        return Response(serializer.data)
    
    def create_jobPosting():
        serializer = JobPostingSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(company=company_info)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    if request.method == 'GET':
        return job_list()
    elif request.method == 'POST':
        return create_jobPosting()


# 상세 조회, 수정, 삭제
@api_view(['GET', 'PUT', 'DELETE'])
def job_detail_or_update_or_delete(request, jobposting_pk):
    jobPosting = get_object_or_404(JobPosting, pk=jobposting_pk)

    def jobPosting_detail():
        serializer = JobPostingSerializer(jobPosting)
        return Response(serializer.data)

    def update_jobPosting():
        serializer = JobPostingSerializer(instance=jobPosting, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
  

    def delete_jobPosting():
        jobPosting.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


    if request.method == 'GET':
        return jobPosting_detail()
    elif request.method == 'PUT':
        if str(request.user) == str(jobPosting.company):
            return update_jobPosting()
     
    elif request.method == 'DELETE':
        if str(request.user) == str(jobPosting.company):
            return delete_jobPosting()



@api_view(['GET'])
def company_detail(request):
    company = get_object_or_404(Company, company_id = request.user.id)
    serializer = CompanySerializer(company)
    return Response(serializer.data)