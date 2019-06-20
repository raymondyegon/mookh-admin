

from django.contrib import admin
from django.urls import path, include
from django.conf.urls import re_path
from django.urls import reverse_lazy
from .views import SchedulingCreateView, SchedulingListView, SchedulingDeleteView, SchedulingUpdateView, SchedulingDetailView, AddEmailGroupCreateView, AddEmailGroupListView, EmailGroupDetailView, AddUsersToGroupUpdateView, emails, SendUserEmails,EmailSchedulingCreateView


urlpatterns = [
    # List and detail views
    re_path(r'^$', SchedulingListView.as_view(), name='list_schedules'),
    re_path(r'^(?P<pk>[0-9]+)$',
            SchedulingDetailView.as_view(),
            name='view_schedules'),
    re_path(r'^(?P<pk>[0-9]+)$',
            EmailGroupDetailView.as_view(),
            name='view_group'),
    re_path(r'^sendgrid/', emails, name='sendgrid'),
    re_path(r'^email-users/', SendUserEmails.as_view(), name='email'),
    
    # Create, update, delete
    path('new/', SchedulingCreateView.as_view(), name='new_schedule'),
    path('new-email/', EmailSchedulingCreateView.as_view(), name='new_emailschedule'),
    path('<int:pk>/edit', SchedulingUpdateView.as_view(), name='edit_schedule'),
    path('<int:pk>/delete', SchedulingDeleteView.as_view(), name='delete_schedule'),
    path('new-group/', AddEmailGroupCreateView.as_view(), name='new_group'),
    path('groups/', AddEmailGroupListView.as_view(), name='group_list'),
    path('<int:pk>/addusers', AddUsersToGroupUpdateView.as_view(), name='edit_group')
]
