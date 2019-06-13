from django.shortcuts import render
from .models import Scheduling
from django.views.generic import CreateView
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.edit import DeleteView
from django.views.generic.edit import UpdateView
from django.views.generic.list import ListView

# Create your views here.
class SchedulingCreateView(SuccessMessageMixin, CreateView):
    """Powers a form to create a new schedule"""

    model = Scheduling
    fields = ['name', 'phone_number', 'time', 'time_zone']
    success_message = 'Schedule successfully created.'
    
class SchedulingListView(ListView):
    """Shows users a list of schedules"""

    model = Scheduling


class SchedulingDetailView(DetailView):
    """Shows users a single schedule"""

    model = Scheduling





class SchedulingUpdateView(SuccessMessageMixin, UpdateView):
    """Powers a form to edit existing schedules"""

    model = Scheduling
    fields = ['name', 'phone_number', 'time', 'time_zone']
    success_message = 'Schedule successfully updated.'


class SchedulingDeleteView(DeleteView):
    """Prompts users to confirm deletion of an schedule"""

    model = Scheduling
    success_url = reverse_lazy('list_schedules')
