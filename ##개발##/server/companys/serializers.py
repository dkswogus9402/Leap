from rest_framework import serializers
from rest_auth.registration.serializers import RegisterSerializer
from .models import  Company

class CompanyCustomRegistrationSerializer(RegisterSerializer):
    company = serializers.PrimaryKeyRelatedField(read_only=True,)
    number_of_workers = serializers.IntegerField(required=True)
    year_of_establishment = serializers.IntegerField(required=True)
    industry = serializers.CharField(required=True)
    company_size = serializers.CharField(required=True)
    
    def get_cleaned_data(self):
            data = super(CompanyCustomRegistrationSerializer, self).get_cleaned_data()
            extra_data = {
                'name' : self.validated_data.get('name', ''),
                'tell' : self.validated_data.get('tell', ''),
                'email' : self.validated_data.get('email', ''),
                'location' : self.validated_data.get('location', ''),
                'number_of_workers' : self.validated_data.get('number_of_workers', ''),
                'year_of_establishment' : self.validated_data.get('year_of_establishment', ''),
                'industry': self.validated_data.get('industry', ''),
                'company_size': self.validated_data.get('company_size', '')
            }
            data.update(extra_data)
            return data

    def save(self, request):
        user = super(CompanyCustomRegistrationSerializer, self).save(request)
        user.is_company = True
        user.save()
        company = Company(
                company=user,
                name = self.cleaned_data.get('name'),
                tell = self.cleaned_data.get('tell'),
                email = self.cleaned_data.get('email'),
                location = self.cleaned_data.get('location'), 
                number_of_workers=self.cleaned_data.get('number_of_workers'), 
                year_of_establishment=self.cleaned_data.get('year_of_establishment'), 
                industry=self.cleaned_data.get('industry'),
                company_size=self.cleaned_data.get('company_size')
                )
        company.save()
        return user

