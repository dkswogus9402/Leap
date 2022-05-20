from rest_framework import serializers
from rest_auth.registration.serializers import RegisterSerializer
from rest_framework.authtoken.models import Token
from .models import Jobseeker
from academys.models import Education
from companys.models import JobPosting

class JobseekerCustomRegistrationSerializer(RegisterSerializer):
    jobseeker = serializers.PrimaryKeyRelatedField(read_only=True,) #by default allow_null = False
    address = serializers.CharField(required=True)
    description = serializers.CharField(required=True)
    # resume = serializers.StringRelatedField(many=True)

    def get_cleaned_data(self):
            data = super(JobseekerCustomRegistrationSerializer, self).get_cleaned_data()
            extra_data = {
                'name' : self.validated_data.get('name', ''),
                'tell' : self.validated_data.get('tell', ''),
                'email' : self.validated_data.get('email', ''),
                'location' : self.validated_data.get('location', ''),
                'address' : self.validated_data.get('address', ''),
                'description': self.validated_data.get('description', ''),
                # 'resume' : self.validated_data.get('resume', ''),
            }
            data.update(extra_data)
            return data

    def save(self, request):
        user = super(JobseekerCustomRegistrationSerializer, self).save(request)
        user.is_jobseeker = True
        user.save()
        jobseeker = Jobseeker(jobseeker=user, 
                name = self.cleaned_data.get('name'),
                tell = self.cleaned_data.get('tell'),
                email = self.cleaned_data.get('email'),
                location = self.cleaned_data.get('location'), 
                address=self.cleaned_data.get('address'),
                description=self.cleaned_data.get('description'),
                resume = self.cleaned_data.get('resume'))
        jobseeker.save()
        return user



class JobseekerSerializer(serializers.ModelSerializer):

    class JobposingSerializer(serializers.ModelSerializer):
        class Meta: 
            model = JobPosting
            fields = "__all__"

    class EducationSerializer(serializers.ModelSerializer):
        class Meta: 
            model = Education
            fields = ("progressing_education", "completed_education")


    progressing_education = EducationSerializer(many=True, read_only=True)
    completed_education = JobposingSerializer(many=True, read_only=True)
    
    class Meta:
        model = Jobseeker
        fields = "__all__"