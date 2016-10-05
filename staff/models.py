from django.db import models
from django.contrib.auth.models import User
from datetime import date


# Create your models here.
class StaffProfile(models.Model):
    staff_name = models.ForeignKey(User, blank=False)
    registration_date = models.DateField('Date submitted', default=date.today())
    home_phone = models.CharField(('home_phone'), max_length=50, blank=True, null=True)
    mobile_phone = models.CharField(('mobile_phone'), max_length=50, blank=True, null=True)
    work_phone = models.CharField(max_length= 50, blank=True, null=True)
    street_address = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(('city'), max_length=255, blank=True, null=True)
    postal_code = models.CharField(('postal'), max_length=50, blank=True, null=True)
    province = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)
    date_of_birth = models.DateField('Date of Birth', null=True, blank=True)