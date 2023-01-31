# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
#from django.contrib.auth.models import User

# Create your models here.
from apps.authentication.models import *
from apps.hr.models import *
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db.models.signals import post_save
from django.dispatch import receiver
import datetime
from birthday import BirthdayField, BirthdayManager
from uuid import uuid4

#
#

#


class Grades(models.Model):
    grade_level = models.CharField(max_length=50)
    fee = models.IntegerField()
    is_semeter = models.BooleanField()

    def __str__(self):
        return self.grade_level

#
#
#
#
# class term(models.Model):


class ClassRoom(models.Model):
    room_name = models.CharField(max_length=50)
    gradeLEVEL = models.ForeignKey(Grades, on_delete=models.CASCADE)
    capacity = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f'{self.room_name} {"/"} {self.gradeLEVEL}'


# المادة
class Subject(models.Model):
    subject_name = models.CharField(max_length=50)
    gradeLEVEL = models.ForeignKey(Grades, on_delete=models.CASCADE)
    is_countable = models.BooleanField(default=True)  # مادة فوق المجموع؟

    def __str__(self):
        return self.subject_name


# ترتيب الجيد والممتاز لكل مادة
class SubjScore(models.Model):
    subject_name = models.ForeignKey(Subject, on_delete=models.CASCADE)
    score_name = models.CharField(max_length=50)
    start_score = models.FloatField()
    end_score = models.FloatField()


#

class TermsOfGrade(models.Model):
    term_name = models.CharField(max_length=50)
    gradeLEVEL = models.ForeignKey(Grades, on_delete=models.CASCADE)
    year = models.CharField(max_length=50, null=True, blank=True)
    start_date = models.DateField()
    end_date = models.DateField()
 
    def __str__(self):
        return f'{self.term_name} {"/"} {self.gradeLEVEL}{"/"} {self.year}'

    def save(self, *args, **kwargs):
        self.year = datetime.datetime.now().strftime("%Y")
        super(TermsOfGrade, self).save(*args, **kwargs)


#############################
##########


class TeacherProfile(EmpProfile):

    user = models.OneToOneField(
        Teacher, on_delete=models.SET_NULL, null=True, blank=True)

    teached_subjects = models.ManyToManyField(Subject, blank=True)
    teached_classRooms = models.ManyToManyField(ClassRoom, blank=True)

    def __str__(self):
        return self.name


#########################################
##########################
#


class GuardianProfile(models.Model):
    # user = models.OneToOneField(guardian, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=250)
    address = models.CharField(max_length=400)
    contact_number = models.CharField(max_length=20)
    emergancy_contact = models.CharField(max_length=20)
    email = models.EmailField(max_length=254, null=True, blank=True)
    citizenship = models.CharField(max_length=50)
    id_num = models.CharField(max_length=50)
    debt = models.FloatField(default=0.00)

    def __str__(self):
        return self.name


##############################################


class StudentProfile(models.Model):
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

    user = models.OneToOneField(
        Student, on_delete=models.SET_NULL, null=True, blank=True)
    student_id = models.CharField(max_length=20, null=True, blank=True)

    current_class = models.ForeignKey(
        ClassRoom, on_delete=models.SET_NULL, null=True, blank=True)
    gradeLEVEL = models.ForeignKey(Grades, on_delete=models.CASCADE)
    is_enrolled = models.BooleanField()

    student_name = models.CharField(max_length=250)
    father_name = models.CharField(max_length=250)
    mother_name = models.CharField(max_length=250)
    present_address = models.CharField(max_length=400)
    contact_number = models.CharField(max_length=20)
    citizenship = models.CharField(max_length=50)
    email_address = models.EmailField(max_length=254, null=True, blank=True)
    birth_date = BirthdayField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    blood_group = models.CharField(max_length=5, choices=BLOOD_CHOICES)
    guardian = models.ForeignKey(GuardianProfile, on_delete=models.CASCADE)
    relation_with_applicant = models.CharField(
        max_length=255, null=True, blank=True)
    student_pic = models.ImageField(
        upload_to="images/studentPic", null=True, blank=True)

    def __str__(self):
        return f'{self.student_id} {"-"} {self.student_name}'

    def save(self, *args, **kwargs):
        queryset = StudentProfile.objects.all()
        if queryset.exists():
            i = StudentProfile.objects.all().count() + 1
            self.student_id = datetime.datetime.now().strftime(
                "%y") + str("%04d" % i)
        else:
            self.student_id = datetime.datetime.now().strftime("%y") + "0001"
        super(StudentProfile, self).save(*args, **kwargs)

#
#
#


class MedicalCondition(models.Model):
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE)
    condition_name = models.CharField(max_length=30)
    desc = models.CharField(max_length=300)


##################################
##################################
##################################
#
# Table for the type of assigments// for example: Quiz-Exam-homework-تسميع-نشاطات
class SubjEvaluTyp(models.Model):
    evalName = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    # wight of this Evaluation type out of the total grade of the Subject
    evaluWight = models.IntegerField()
    year = models.CharField(max_length=50)

    def save(self, *args, **kwargs):
        self.year = datetime.datetime.now().strftime("%Y")
        super(SubjEvaluTyp, self).save(*args, **kwargs)

    def __str__(self):
        return self.evalName


#
# here is the assigment itself:
class Evaluation(models.Model):
    evaluTyp = models.ForeignKey(SubjEvaluTyp, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    evalName = models.CharField(max_length=50)
    tot_grade = models.FloatField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    is_Extra_Credit = models.BooleanField(default=False)

    def __str__(self):
        return self.evalName


# درجة الطالب في كل امتحان او تطبيق
class Result(models.Model):
    subjEvalu = models.ForeignKey(Evaluation, on_delete=models.CASCADE)
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE)
    result = models.FloatField()
    result_wight = models.FloatField()

    date = models.CharField(max_length=50)
    grade_level = models.CharField(max_length=50)

    def save(self, *args, **kwargs):
        self.date = datetime.datetime.now().strftime("%d %B, %Y")
        self.grade_level = self.student.gradeLEVEL.grade_level
        super(Result, self).save(*args, **kwargs)


#
# الدرجة النهائية لطالب بالمادة
class TotResult(models.Model):
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    tot_result = models.FloatField()
    term = models.CharField(max_length=50, null=True, blank=True)
    grade_level = models.CharField(max_length=50, null=True, blank=True)

    def save(self, *args, **kwargs):
        now = datetime.datetime.now().strftime("%Y-%m-%d")
        self.grade_level = self.student.gradeLEVEL.grade_level
        tt = TermsOfGrade.objects.filter(gradeLEVEL__grade_level=self.grade_level).get(
            start_date__lt=now, end_date__gt=now)
        self.term = tt.term_name

        super(TotResult, self).save(*args, **kwargs)


# الواجبات
# class Assignment(models.Model):
 #   teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
  #  subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

# صحيفة السيمستر او الفترة
class StudentTerm(models.Model):
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE)
    term = models.ForeignKey(TermsOfGrade, on_delete=models.CASCADE)
    # درجة السيمتر/السنة  بالحروف مثال: ممتاز/جيد/مقبول/ساقط
    termGrade = models.CharField(max_length=50, null=True,
                                 blank=True)
    term_Result = models.FloatField()  # درجة المجموع لهذا السيمستر/السنة
    rank = models.CharField(max_length=50, null=True,
                            blank=True)  # ترتيب الطالب علي الفصل

    def save(self, *args, **kwargs):
        tt = SubjScore.objects.get(
            start_score__lt=self.term_Result, end_score__gt=self.term_Result)
        self.termGrade = tt.score_name

        super(StudentTerm, self).save(*args, **kwargs)

#
#

#


###########################################################
######################################################
#########################################################################
##################################################################################
#                            الجانب المالي
############################################################################


class PaymentPlan(models.Model):
    plan_name = models.CharField(max_length=50)
    divition_factor = models.PositiveIntegerField()

    def __str__(self):
        return self.plan_name


#
# اشتراك باص او اي نوع من خدمات زيادة
class Services(models.Model):
    service_name = models.CharField(max_length=50)
    service_price = models.FloatField()

    def __str__(self):
        return f'{self.service_name} {"-"} {self.service_price}'


class FeeInvoice(models.Model):
    STATUS_CHOICES = (('PENDING', 'Pending'),
                      ('PARTIALLY PAID', 'Partially Paid'),
                      ('PAID', 'Paid')
                      )

    #guardian = models.ForeignKey(GuardianProfile, on_delete=models.CASCADE)
    #student = models.CharField(max_length=50)
    guardian = models.CharField(max_length=50)
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE)
    admission_fee = models.FloatField()
    services = models.ManyToManyField(Services, blank=True)
    tot_amount = models.FloatField()
    discount = models.FloatField(default=0.00)
    payment_Plan = models.ForeignKey(PaymentPlan, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=50, choices=STATUS_CHOICES, default='Pending')


#

class FeePaymant(models.Model):
    STATUS2_CHOICES = (('PENDING', 'Pending'),
                       ('PAID', 'Paid')
                       )

    fee_invoice = models.ForeignKey(FeeInvoice, on_delete=models.CASCADE)
    due_amount = models.FloatField()
    created_date = models.CharField(max_length=50)
    due_date = models.CharField(max_length=50)
    until_due_date = models.IntegerField()
    status = models.CharField(
        max_length=50, choices=STATUS2_CHOICES, default='Pending')
   # payment_method = models.CharField(max_length=50,)
#
#


# في حال الطالب كسر شي لازم يخلصه// يتم اضافته الي الفاتورة
class FineInvoice(models.Model):
    STATUS3_CHOICES = (('PENDING', 'Pending'),
                       ('PAID', 'Paid')
                       )
    name = models.CharField(max_length=50)
    descraption = models.CharField(max_length=500)
    guardian = models.CharField(max_length=50)
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE)
    amount = models.FloatField()
    status = models.CharField(
        max_length=50, choices=STATUS3_CHOICES, default='Pending')


class FinePaymant(models.Model):
    STATUS4_CHOICES = (('PENDING', 'Pending'),
                       ('PAID', 'Paid')
                       )

    fine_invoice = models.ForeignKey(FineInvoice, on_delete=models.CASCADE)
    due_amount = models.FloatField()
    created_date = models.CharField(max_length=50)
    status = models.CharField(
        max_length=50, choices=STATUS4_CHOICES, default='Pending')
