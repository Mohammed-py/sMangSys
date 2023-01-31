# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""
from django.contrib.auth import get_user_model, forms
from django import forms
from django.contrib.auth.forms import UserCreationForm
#from django.contrib.auth.models import User
from .models import *
from django.db import transaction

User = get_user_model()


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Username",
                "class": "form-control"
            }
        ))
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password",
                "class": "form-control"
            }
        ))


class SignUpUserForm(UserCreationForm):

    USER_TYPE = (
        ("ADMIN", "Admin"),
        ("STUDENT", "Student"),
        ("TEACHER", "Teacher"),)

    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Username",
                "class": "form-control"
            }
        ))
    #user_type = forms.ChoiceField(choices=USER_TYPE)

    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password",
                "class": "form-control"
            }
        ))
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password check",
                "class": "form-control"
            }
        ))

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')


class SignUpStudentForm(UserCreationForm):

    
    USER_TYPE = (
        ("ADMIN", "Admin"),
        ("STUDENT", "Student"),
        ("TEACHER", "Teacher"), ( "STAFF", "Staff"),)

    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Username",
                "class": "form-control"
            }
        ))
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "placeholder": "Email",
                "class": "form-control"
            }
        ))
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password",
                "class": "form-control"
            }
        ))
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password check",
                "class": "form-control"
            }
        ))

    #type = forms.ChoiceField(choices=USER_TYPE)
    

    class Meta:
        model = Student
        fields = ('username', 'email', 'password1', 'password2',)


class SignUpTeacherForm(UserCreationForm):

    USER_TYPE = (
        ("ADMIN", "Admin"),
        ("STUDENT", "Student"),
        ("TEACHER", "Teacher"),
        ( "STAFF", "Staff"),)

    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Username",
                "class": "form-control"
            }
        ))
    #user_type = forms.ChoiceField(choices=USER_TYPE)

    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password",
                "class": "form-control"
            }
        ))
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password check",
                "class": "form-control"
            }
        ))

    class Meta:
        model = Teacher
        fields = ('username', 'email', 'password1', 'password2')



class SignUpStaffForm(UserCreationForm):

    
    USER_TYPE = (
        ("ADMIN", "Admin"),
        ("STUDENT", "Student"),
        ("TEACHER", "Teacher"), ( "STAFF", "Staff"),)

    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Username",
                "class": "form-control"
            }
        ))
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "placeholder": "Email",
                "class": "form-control"
            }
        ))
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password",
                "class": "form-control"
            }
        ))
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password check",
                "class": "form-control"
            }
        ))

    #type = forms.ChoiceField(choices=USER_TYPE)
    

    class Meta:
        model = Staff
        fields = ('username', 'email', 'password1', 'password2',)

