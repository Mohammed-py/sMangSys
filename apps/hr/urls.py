# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from .views import *
from apps.home import views


app_name = "hr"
urlpatterns = [

    # The home page
    # path('', views.hrIndex, name='home'),
    path('', dashboard, name='dahsboard'),
    path('allEmp/', EmpView.as_view(), name='emplist'),
    path('teacher/<slug:slug>', TeacherDetailView.as_view(), name='teacher-detail'),
    path('staff/<slug:slug>', StaffDetailView.as_view(), name='staff-detail'),
    path('toooest/', views.index_old, name='st'),
    path('conf/', configView, name='confiHR'),

    # Matches any html file
    #re_path(r'^.*\.*', views.pages, name='pages'),

]
