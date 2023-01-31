# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, include
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', login_view, name="login"),

    #      REGISTER
    path('register/', register_user, name="register"),
    path('stu-reg/', register_student, name="studentregister"),
    path('teacher-reg/', register_teacher, name="teacherregister"),
    path('staff-reg/', register_staff, name="staffregister"),



    # path('register2/', SignUpView2.as_view(), name="register2"),
    #path('register2/', StudentSignUpView.as_view(), name="register2"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path('social_login/', include('allauth.urls')),
]
