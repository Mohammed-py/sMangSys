# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from .models import *

# Register your models here.


# class TeacherProfile(admin.ModelAdmin): list_display = ('name', 'phoneNum', 'typpe', 'location', 'balance') search_fields = ('phoneNum',)


#admin.site.register(Agent, AgentAdmin)

admin.site.register(StaffProfile)
admin.site.register(LeavesType)
admin.site.register(DaysOff)
admin.site.register(Departments)
admin.site.register(EmpProfile)
admin.site.register(EmpLeaveRecord)
admin.site.register(EmpLeaveRequest)
