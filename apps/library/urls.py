from django.urls import path
from .views import *


app_name = "library"


urlpatterns = [
    path('', allbooks, name='library_home'),

]
