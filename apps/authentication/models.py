# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.urls import reverse


############################################################################################


#####################


# class User(AbstractUser, PermissionsMixin):
# class User(AbstractUser):
#   USER_TYPE_CHOICES = (
#       ("ADMIN", "Admin"),
#      ("STUDENT", "Student"),
#     ("TEACHER", "Teacher"),)

# base_role = Role.ADMIN

#email = models.EmailField(gettext_lazy('email address'), unique=True)
#user_name = models.CharField(max_length=150, unique=True)
#first_name = models.CharField(max_length=150, blank=True)
#start_date = models.DateTimeField(default=timezone.now)

#is_staff = models.BooleanField(default=False)
# is_active = models.BooleanField(default=False)
#  user_type = models.CharField(max_length=50, choices=USER_TYPE_CHOICES)

#objects = CustomerUserManager()

#USERNAME_FIELD = 'user_name'
#REQUIRED_FIELDS = ['email', 'first_name']

# def __str__(self):
#    return self.user_name


########################################################################
#  def save(self, *args, **kwargs):
#     if not self.pk:
#        self.role = self.base_role
#       return super().save(*args, **kwargs)


# class StudentManager(BaseUserManager):
#  def get_queryset(self, *args, **kwargs):
#    results = super().get_queryset(*args, **kwargs)
#     return results.filter(role=User.Role.STUDENT)


# class Student(User):

#   base_role = User.Role.STUDENT

#  student = StudentManager()

# class Meta:
#    proxy = True

# def welcome(self):
#   return "Only for students"


# @receiver(post_save, sender=Student)
# def create_user_profile(sender, instance, created, **kwargs):
#    if created and instance.role == "STUDENT":
#        StudentProfile.objects.create(user=instance)


# class TeacherManager(BaseUserManager):
#   def get_queryset(self, *args, **kwargs):
#      results = super().get_queryset(*args, **kwargs)
#     return results.filter(role=User.Role.TEACHER)


# class Teacher(User):

#   base_role = User.Role.TEACHER

#  teacher = TeacherManager()

# class Meta:
#    proxy = True

# def welcome(self):
#   return "Only for teachers"


# @receiver(post_save, sender=Teacher)
# def create_user_profile(sender, instance, created, **kwargs):
#    if created and instance.role == "TEACHER":
#        TeacherProfile.objects.create(user=instance)


#######################
##########

class User(AbstractUser):
    class Types(models.TextChoices):
        ADMIN = "ADMIN", "Admin"
        STUDENT = "STUDENT", "Student"
        TEACHER = "TEACHER", "Teacher" 
        STAFF = "STAFF", "Staff" 

    base_type = Types.ADMIN

    # What type of user are we?
    type = models.CharField(
        _("Type"), max_length=50, choices=Types.choices, default=base_type
    )

    # First Name and Last Name Do Not Cover Name Patterns
    # Around the Globe.
    name = models.CharField(_("Name of User"), blank=True, max_length=255)

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})

    def save(self, *args, **kwargs):
        if not self.id:
            self.type = self.base_type
        return super().save(*args, **kwargs)


class StudentManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=User.Types.STUDENT)

    def create_user(self, email, full_name=None, password=None,):# is_active=True, is_staff=False, is_admin=False):
        if not email:
            raise ValueError("Users must have an email address")
        if not password:
            raise ValueError("Users must have a password")
        user_obj = self.model(
            email=self.normalize_email(email),
            full_name=full_name,
            
        )
        user_obj.set_password(password)  # change user password
        #user_obj.staff = is_staff
        #user_obj.admin = is_admin
        #user_obj.active = is_active
        user_obj.type= "STUDENT"
        user_obj.save(using=self._db)
        return user_obj


class TeacherManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=User.Types.TEACHER)

    def create_user(self, email, full_name=None, password=None, is_active=True, is_staff=False, is_admin=False):
        if not email:
            raise ValueError("Users must have an email address")
        if not password:
            raise ValueError("Users must have a password")
        user_obj = self.model(
            email=self.normalize_email(email),
            full_name=full_name,
            type="TEACHER"
        )
        user_obj.set_password(password)  # change user password
        user_obj.staff = is_staff
        user_obj.admin = is_admin
        user_obj.active = is_active
        user_obj.save(using=self._db)
        return user_obj


class StaffManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=User.Types.TEACHER)

    def create_user(self, email, full_name=None, password=None, is_active=True, is_staff=False, is_admin=False):
        if not email:
            raise ValueError("Users must have an email address")
        if not password:
            raise ValueError("Users must have a password")
        user_obj = self.model(
            email=self.normalize_email(email),
            full_name=full_name,
            type="STAFF"
        )
        user_obj.set_password(password)  # change user password
        user_obj.staff = is_staff
        user_obj.admin = is_admin
        user_obj.active = is_active
        user_obj.save(using=self._db)
        return user_obj



#######
class Student(User):
    base_type = User.Types.STUDENT
    objects = StudentManager()

    class Meta:
        proxy = True

        
    def save(self, *args, **kwargs):
        self.type = User.Types.STUDENT
       # self.is_student = True
        return super().save(*args , **kwargs)
       


class Teacher(User):
    base_type = User.Types.TEACHER
    objects = TeacherManager()

    class Meta:
        proxy = True

    def accelerate(self):
        return "Go faster"

    def save(self, *args, **kwargs):
        if not self.id:
            self.type = self.TEACHER
        return super().save(*args, **kwargs)


class Staff(User):
    base_type = User.Types.STAFF
    objects = StaffManager()

    class Meta:
        proxy = True

    def accelerate(self):
        return "Go faster"

    def save(self, *args, **kwargs):
        if not self.id:
            self.type = self.STAFF
        return super().save(*args, **kwargs)
