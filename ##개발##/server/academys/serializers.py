from rest_framework import serializers
from rest_auth.registration.serializers import RegisterSerializer
from .models import Academy


class AcademyCustomRegistrationSerializer(RegisterSerializer):
    name = serializers.CharField(max_length = 20) # 가입자 이름
    tell = serializers.CharField(max_length = 13) # 전화번호
    email = serializers.CharField(max_length = 255) # 이메일
    location = serializers.CharField(max_length = 255) # 회사 위치
    academy = serializers.PrimaryKeyRelatedField(read_only=True,) #by default allow_null = False
    CEO = serializers.CharField(required=True)
    site = serializers.CharField(max_length=255) # 홈페이지 주소
    def get_cleaned_data(self):
            data = super(AcademyCustomRegistrationSerializer, self).get_cleaned_data()
            extra_data = {
                'name' : self.validated_data.get('name', ''),
                'tell' : self.validated_data.get('tell', ''),
                'email' : self.validated_data.get('email', ''),
                'location' : self.validated_data.get('location', ''),
                'CEO' : self.validated_data.get('CEO', ''),
                'site' : self.validated_data.get('site', '')
            }
            data.update(extra_data)
            return data

    def save(self, request):
        user = super(AcademyCustomRegistrationSerializer, self).save(request)
        user.is_academy = True
        user.save()
        academy = Academy(academy=user,
            name = self.cleaned_data.get('name'),
            tell = self.cleaned_data.get('tell'),
            email = self.cleaned_data.get('email'),
            location = self.cleaned_data.get('location'),
            CEO=self.cleaned_data.get('CEO'),
            site=self.cleaned_data.get('site')
        )
        academy.save()
        return user