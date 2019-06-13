

from django.contrib import admin
from django.urls import path, include
from .views import SchedulingCreateView



urlpatterns = [
    path(r'^new$', SchedulingCreateView.as_view(), name='new_scheduling'),
]


