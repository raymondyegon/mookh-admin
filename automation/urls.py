

from django.contrib import admin
from django.urls import path, include
from django.conf.urls import re_path
from django.urls import reverse_lazy
from .views import SchedulingCreateView, SchedulingListView, SchedulingDeleteView, SchedulingUpdateView, SchedulingDetailView



urlpatterns = [
    # List and detail views
    re_path(r'^$', SchedulingListView.as_view(), name='list_schedules'),
    re_path(r'^(?P<pk>[0-9]+)$',SchedulingDetailView.as_view(),name='view_schedules'),
    path('new/', SchedulingCreateView.as_view(), name='new_schedule'),
    # Create, update, delete
    # re_path(r'^new$', SchedulingCreateView.as_view(), name='new_schedule'),
    re_path(r'^(?P<pk>[0-9]+)/edit$',SchedulingUpdateView.as_view(),name='edit_schedule'),
    re_path(r'^(?P<pk>[0-9]+)/delete$',SchedulingDeleteView.as_view(),name='delete_schedule'),
]


