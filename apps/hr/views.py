# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import template
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import *
from .forms import *
from .filters import *
from apps.admission.models import *
###
from django.http import JsonResponse
from django.shortcuts import render
from django.core import serializers
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
import json


##############


def dashboard(request):
    # using [:4] to limit the query to only showing first 4
    levTy = LeavesType.objects.all()[:4]
    dyff = DaysOff.objects.all()[:4]
    dep = Departments.objects.all()[:4]
    empLeaveRequest = EmpLeaveRequest.objects.all()[:6]
    empProfile = EmpProfile.objects.all()[:6]
    #teacherProfile = TeacherProfile.objects.all()[:6]

    data = {
        "levTy": levTy,
        "dyff": dyff,
        "dep": dep,
        "empLeaveRequest": empLeaveRequest,
        "empProfile": empProfile,
        # "teacherProfile": teacherProfile,

    }
    return render(request, "hr/dahsboard.html", data)


class EmpView(ListView):
    model = EmpProfile
    context_object_name = 'topics'
    paginate_by = 6
    template_name = 'hr/emp_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['filter'] = EmpProfileFilter(
            self.request.GET, queryset=self.get_queryset())
        teachers = TeacherProfile.objects.all()
        stafff = StaffProfile.objects.all()
        context += teachers + stafff
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        return EmpProfileFilter(self.request.GET, queryset=queryset).qs


class StaffDetailView(DetailView):

    model = StaffProfile
    template_name = 'hr/staff_profile.html'
    context_object_name = 'staff'

    def get_success_url(self):
        return reverse('detail', kwargs={'slug': self.slug})


class TeacherDetailView(DetailView):

    model = TeacherProfile
    template_name = 'hr/teacher_profile.html'
    context_object_name = 'teacher'

    def get_success_url(self):
        return reverse('detail', kwargs={'slug': self.slug})


def configView(request):

    depForm = DepartmentsForm()
    fDayForm = DaysOffForm()
    leavTyForm = LeavesTypeForm()

    data = {"depForm": depForm, "fDayForm": fDayForm,
            "leavTyForm": leavTyForm, }
    return render(request, "hr/config.html", data)


# def zeroingBalances(request):
 #   holders = CardHolder.objects.all()
  #  print("TTTTTTTTTT")
   # if request.method == "POST":
    #    id_list = request.POST.getlist('boxes')
#
 #       for x in id_list:
  #          CardHolder.objects.filter(pk=int(x)).update(balance=0.00)
   #     messages.warning(
    #        request, ' الصحيحة ')
    #   return render(request, "/")
#
 #   data = {"holders": holders, }
#
 #   return render(request, "main/zeroing_balances.html", data)
