from django.db import models
from ..companys.models import JobPosting
from ..academys.models import Education
# Create your models here.
class Certification(models.Model):
    # M : N 관계
    edu_certification = models.ManyToManyField(Education, related_name='certification_edu')
    # M : N 관계
    posting_certification = models.ManyToManyField(JobPosting, related_name='certification_posting')
    name = models.CharField(max_length=45)