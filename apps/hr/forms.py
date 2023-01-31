from django import forms
from .models import *
from django.contrib.auth.models import Group, Permission
from django.contrib.admin.widgets import FilteredSelectMultiple


class DepartmentsForm(forms.ModelForm):

    class Meta:
        model = Departments
        fields = '__all__'


class DaysOffForm(forms.ModelForm):

    class Meta:
        model = DaysOff
        fields = '__all__'


class LeavesTypeForm(forms.ModelForm):

    class Meta:
        model = LeavesType
        fields = '__all__'
