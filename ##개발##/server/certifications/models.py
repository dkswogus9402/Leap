from django.db import models
from django.conf import settings
# Create your models here.
class Certification(models.Model):
    # M : N 관계
    edu_certification = models.ManyToManyField(settings.EDUCATION_MODEL, related_name='certification_edu')
    # M : N 관계
    posting_certification = models.ManyToManyField(settings.JOBPOSTING_MODEL, related_name='certification_posting')
    name = models.CharField(max_length=45)