# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from .views import *
from apps.hr import views


app_name = "home"
urlpatterns = [

    # The home page
    path('', index, name='home'),
    path('old/', index_old, name='home_old'),
    #path('toooest333/', testN, name='st2'),


    # Matches any html file
    re_path(r'^.*\.*', pages, name='pages'),

]
