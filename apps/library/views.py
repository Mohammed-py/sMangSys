
from django.shortcuts import render, redirect
from .models import *
from apps.authentication.models import Student
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.contrib import messages
from django.utils import timezone
import datetime

from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib import auth
from core import settings

#
# Book
def allbooks(request):
   # requestedbooks, issuedbooks = getmybooks(request.user)
    allbooks = Book.objects.all()

    return render(request, 'library/home.html', {'books': allbooks, })
