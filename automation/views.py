from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import DeleteView
from django.views.generic.edit import UpdateView
from django.views.generic.list import ListView

from .models import Appointment


class AppointmentListView(ListView):
    """Shows users a list of appointments"""

    model = Appointment


class AppointmentDetailView(DetailView):
    """Shows users a single appointment"""

    model = Appointment


class AppointmentCreateView(SuccessMessageMixin, CreateView):
    """Powers a form to create a new appointment"""

    model = Appointment
    fields = ['name', 'phone_number', 'time', 'time_zone']
    success_message = 'Appointment successfully created.'


class AppointmentUpdateView(SuccessMessageMixin, UpdateView):
    """Powers a form to edit existing appointments"""

    model = Appointment
    fields = ['name', 'phone_number', 'time', 'time_zone']
    success_message = 'Appointment successfully updated.'


class AppointmentDeleteView(DeleteView):
    """Prompts users to confirm deletion of an appointment"""

    model = Appointment
    success_url = reverse_lazy('list_appointments')


# ## Download the Python helper library from twilio.com/docs/python/install 
# from twilio.rest import TwilioRestClient

# # Your Account Sid and Auth Token from twilio.com/user/account
# account_sid = "{{ account_sid }}"
# auth_token  = "{{ auth_token }}"
# client = TwilioRestClient(account_sid, auth_token)

# message = client.messages.create(
#     body="Jenny please?! I love you <3",
#     to="+15558675309",
#     from_="+14158141829",
#     media_url="http://www.example.com/hearts.png")
# print message.sid
