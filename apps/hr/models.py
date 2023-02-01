# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from email.policy import default
from urllib import request
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from apps.authentication.models import *
# from apps.admission import models  # import Subject

from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db.models.signals import post_save
from django.dispatch import receiver
import datetime
from birthday import BirthdayField, BirthdayManager
from uuid import uuid4
from django.template.defaultfilters import slugify

#
#
GENDER_CHOICES = (
    ('MALE', 'Male'),
    ('FEMALE', 'Female'),
)
BLOOD_CHOICES = (
    ('A+', 'A+'),
    ('A-', 'A-'),
    ('B+', 'B+'),
    ('B-', 'B-'),
    ('AB+', 'AB+'),
    ('AB-', 'AB-'),
    ('O+', 'O+'),
    ('O-', 'O-'),
)
STATUS_CHOICES = (
    ('PENDING', 'pending'),
    ('APPROVED', 'approved'),
    ('DENIED', 'denied'),
)


#####
##
#

class Departments(models.Model):
    dep_name = models.CharField(max_length=50)

    def __str__(self):
        return self.dep_name

# العطل الرسمية والاعياد


class DaysOff(models.Model):
    days_name = models.CharField(max_length=50)
    descraption = models.CharField(max_length=500)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.days_name


class LeavesType(models.Model):
    days_name = models.CharField(max_length=50)
    descraption = models.CharField(max_length=500)
    num_of_days = models.IntegerField()
    for_all_genders = models.BooleanField(default=True)
    tot_allowed_days = models.IntegerField()

    def __str__(self):
        return self.days_name


#############################
###############
######
#


class EmpProfile(models.Model):
    slug = models.SlugField(null=True, blank=True)

  #  user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=True)
    emp_id = models.IntegerField(null=True, blank=True)
    manager = models.ForeignKey(
        'self', on_delete=models.SET_NULL, null=True, blank=True)
    #
    id_number = models.CharField(max_length=50)
    name = models.CharField(max_length=250)
    address = models.CharField(max_length=400)
    contact_number = models.CharField(max_length=20)
    email = models.EmailField(max_length=254, null=True, blank=True)
    birth_date = BirthdayField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    blood_group = models.CharField(max_length=5, choices=BLOOD_CHOICES)
    joining_date = models.DateField()
    position = models.CharField(max_length=100)
    department = models.ForeignKey(
        Departments, on_delete=models.SET_NULL, null=True, blank=True, related_name="employees")
    emp_status = models.CharField(max_length=70)
    salary = models.IntegerField(null=True, blank=True)
    #profile_image = models.ImageField(upload_to='HR/static/HR')
    #contract_upload = models.FileField(upload_to='HR/static/HR')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        queryset = EmpProfile.objects.all()
        if queryset.exists():
            i = EmpProfile.objects.all().count() + 1
            self.emp_id = datetime.datetime.now().strftime(
                "%y") + str("%03d" % i)
        else:
            self.emp_id = datetime.datetime.now().strftime("%y") + "001"

        if not self.slug:
            self.slug = slugify(self.name)

        super(EmpProfile, self).save(*args, **kwargs)


#################################################
####################


class EmpLeaveRequest(models.Model):
    leave_req_id = models.CharField(max_length=15, null=True, blank=True)
    employee = models.ForeignKey(
        EmpProfile, on_delete=models.CASCADE)
    leaveType = models.ForeignKey(
        LeavesType, on_delete=models.CASCADE)
    days_name = models.CharField(max_length=50)
    descraption = models.CharField(max_length=500, null=True, blank=True)
    start_date = models.DateField()
    end_date = models.DateField()
    num_of_days = models.IntegerField()
    status = models.CharField(
        max_length=35, choices=STATUS_CHOICES, default='pending')
    approved_by = models.CharField(max_length=100, blank=True)

    def save(self, *args, **kwargs):
        queryset = EmpLeaveRequest.objects.all()
        if queryset.exists():
            i = EmpLeaveRequest.objects.all().count() + 1
            self.leave_req_id = datetime.datetime.now().strftime(
                "%y") + str("%04d" % i)
        else:
            self.leave_req_id = datetime.datetime.now().strftime("%y") + "0001"
        super(EmpLeaveRequest, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.employee} {self.leaveType} {self.pk}'


class EmpLeaveRecord(models.Model):
    emp = models.ManyToManyField(EmpProfile,  blank=False)
    leaveTyp = models.ManyToManyField(LeavesType, blank=False)
    tot_days_left = models.IntegerField()

    def __str__(self):
        return f'{self.emp} {self.leaveTyp}'


######################################################################
#####################################
#############


class StaffProfile(EmpProfile):

<<<<<<< HEAD
    user = models.OneToOneField( User, on_delete=models.SET_NULL, null=True, blank=True)
    emp_type = models.CharField(default="staff", max_length=50)

=======
    user = models.OneToOneField(
<<<<<<< HEAD
        User, on_delete=models.SET_NULL, null=True, blank=True)
    emp_type = models.CharField(default="staff", max_length=50)
=======
        Staff, on_delete=models.SET_NULL, null=True, blank=True)
>>>>>>> master
>>>>>>> master

    def __str__(self):
        return self.name
