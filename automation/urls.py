

from django.contrib import admin
from django.urls import path, include
from django.conf.urls import re_path
from .views import SchedulingCreateView



urlpatterns = [
    re_path(r'^new$', SchedulingCreateView.as_view(), name='new_schedule'),
]


