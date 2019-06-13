from django.shortcuts import render
from .models import Scheduling

# Create your views here.
class SchedulingCreateView(SuccessMessageMixin, CreateView):
    """Powers a form to create a new appointment"""

    model = Scheduling
    fields = ['name', 'phone_number', 'time', 'time_zone']
    success_message = 'Appointment successfully created.'
