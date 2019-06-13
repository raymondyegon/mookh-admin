

from django.contrib import admin
from django.urls import path, include
from django.conf.urls import re_path
from .views import SchedulingCreateView, SchedulingListView, SchedulingDeleteView, SchedulingUpdateView, SchedulingDetailView



urlpatterns = [
    path('new/', SchedulingCreateView.as_view(), name='new_schedule'),
    # re_path(r'^new$', SchedulingCreateView.as_view(), name='new_schedule'),
    re_path(r'^$', SchedulingListView.as_view(), name='list_schedules'),
]


