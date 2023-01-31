# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .forms import *
from core.settings import GITHUB_AUTH
from django.views.generic import CreateView
from .models import *
from django.contrib.auth import get_user_model


User = get_user_model()


#

def login_view(request):
    form = LoginForm(request.POST or None)

    msg = None

    if request.method == "POST":

        if form.is_valid():

            username = form.cleaned_data.get("username")
            #email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            #user = authenticate(email=email, password=password)
            if user is not None:
                usserr = User.objects.get(username=username)
                if usserr.type == "TEACHER":
                    login(request, user)
                    return redirect('/library')

                else:
                    login(request, user)
                    return redirect("/")
            else:
                msg = 'Invalid credentials'
        else:
            msg = 'Error validating the form'

    return render(request, "accounts/login.html", {"form": form, "msg": msg, "GITHUB_AUTH": GITHUB_AUTH})


def register_user(request):
    msg = None
    success = False

    if request.method == "POST":
        form = SignUpUserForm(request.POST)
        if form.is_valid():
            form.type = "TEACHER"
            form.save()
           # username = form.cleaned_data.get("username")
            #raw_password = form.cleaned_data.get("password1")
            #user = authenticate(username=username, password=raw_password)

          #  msg = 'User created successfully.'
         #   success = True

            return redirect("/login/")

        else:
            msg = 'Form is not valid'
    else:
        form = SignUpUserForm()

    return render(request, "accounts/register.html", {"form": form, "msg": msg, "success": success})


def register_student(request):
    msg = None
    success = False

    if request.method == "POST":
        form = SignUpStudentForm(request.POST)
        if form.is_valid():
            print("form is Valid   ============================================================")
            #form = SignUpStudentForm(initial={'type': 'STUDENT'})
            form.type = "STUDENT"
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)

            msg = 'User created successfully.'
            success = True

            return redirect("/")

        else:
            print("form is NOOOOOOOOOOOOOOOOOOOOOTTTTT Valid   ============================================================")
            msg = 'Form is not valid'
    else:
        form = SignUpStudentForm()

    return render(request, "accounts/Student_Register.html", {"form": form, "msg": msg, "success": success})





def register_teacher(request):
    msg = None
    success = False

    if request.method == "POST":
        form = SignUpTeacherForm(request.POST)
        if form.is_valid():

            form.type = "TEACHER"
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)

            msg = 'User created successfully.'
            success = True

            return redirect("/")

        else:
            msg = 'Form is not valid'
    else:
        form = SignUpTeacherForm()

    return render(request, "accounts/Teacher_Register.html", {"form": form, "msg": msg, "success": success})






def register_staff(request):
    msg = None
    success = False

    if request.method == "POST":
        form = SignUpStaffForm(request.POST)
        if form.is_valid():

            form.type = "STAFF"
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)

            msg = 'User created successfully.'
            success = True

            return redirect("/")

        else:
            msg = 'Form is not valid'
    else:
        form = SignUpStaffForm()

    return render(request, "accounts/Staff_Register.html", {"form": form, "msg": msg, "success": success})





