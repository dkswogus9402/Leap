
from rest_auth.registration.views import RegisterView
from .serializers import AcademyCustomRegistrationSerializer, CategorySerializer, EducationSerializer, EducationListSerializer

from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import Education, Academy, Category

from django.shortcuts import get_object_or_404


# 로그인 관련
class AcademyRegistrationView(RegisterView):
    serializer_class = AcademyCustomRegistrationSerializer


# 전체조회 및 생성
@api_view(['GET', 'POST'])
def education_list_or_create(request):
    academy_info = get_object_or_404(Academy, academy_id=request.user.id)

    def education_list():
        educations = Education.objects.order_by('-pk')
        serializer = EducationListSerializer(educations, many=True)
        return Response(serializer.data)

    def education_create():
        
        serializer = EducationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(academy=academy_info)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


    if request.method == 'GET':
        return education_list()
    elif request.method == 'POST':
        return education_create()


# 상세 조회, 수정, 삭제 
@api_view(['GET', 'PUT', 'DELETE'])
def education_detail_or_update_or_delete(request, education_pk):
    education = get_object_or_404(Education, pk=education_pk)
    print(request.user)
    print(education.academy)

    def education_detail():
        serializer = EducationSerializer(education)
        return Response(serializer.data)

    def update_education():
        serializer = EducationSerializer(instance=education, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    def delete_education():
        education.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    if request.method == 'GET':
        return education_detail()
    elif request.method == 'PUT':
        if str(request.user) == str(education.academy):
            return update_education()
    elif request.method == 'DELETE':
        if str(request.user) == str(education.academy):
            return delete_education()



# Category 조회 및 생성
@api_view(['GET', 'POST'])
def category_list_or_create(request):

    def category_list():
        categorys = Category.objects.all()
        serializers = CategorySerializer(categorys, many=True)
        return Response(serializers.data)

    def category_create():
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    if request.method == 'GET':
        return category_list()
    elif request.method == 'POST':
        return category_create()


def category_detail_or_update_or_delete(request, category_pk):
    category = get_object_or_404(Education, pk=category_pk)

    def category_detail():
        serializer = CategorySerializer(category)
        return Response(serializer.data)

    def update_category():
        serializer = CategorySerializer(instance=category, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    def delete_category():
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    if request.method == 'GET':
        return category_detail()
    elif request.method == 'PUT':
        return update_category()
    elif request.method == 'DELETE':
        return delete_category()
