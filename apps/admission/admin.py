# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from .models import *

# Register your models here.


# class TeacherProfile(admin.ModelAdmin): list_display = ('name', 'phoneNum', 'typpe', 'location', 'balance') search_fields = ('phoneNum',)
class StudentProfileAdmin(admin.ModelAdmin):
    list_display = ('student_name', 'student_id',)


#admin.site.register(Agent, AgentAdmin)

admin.site.register(GuardianProfile)
admin.site.register(StudentProfile, StudentProfileAdmin)
admin.site.register(TeacherProfile)
admin.site.register(Subject)
admin.site.register(ClassRoom)
admin.site.register(Grades)
admin.site.register(StudentTerm)
admin.site.register(TotResult)
admin.site.register(Result)
admin.site.register(Evaluation)
admin.site.register(SubjEvaluTyp)
admin.site.register(TermsOfGrade)
