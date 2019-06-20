import os
from django.shortcuts import render
from .models import Scheduling, EmailGroup, AddUser, SchedulingEmails
from django.views.generic import CreateView
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import DetailView, FormView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.edit import DeleteView
from django.views.generic.edit import UpdateView
from django.views.generic.list import ListView
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import From, To, PlainTextContent, HtmlContent, Mail
from .forms import SendEmailForm
# Create your views here.


class SchedulingCreateView(SuccessMessageMixin, CreateView):
    """Powers a form to create a new schedule"""

    model = Scheduling
    fields = ['name', 'phone_number', 'time', 'time_zone']
    success_message = 'Schedule successfully created.'
    success_url = reverse_lazy('list_schedules')


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
    success_url = reverse_lazy('view_schedules')


class SchedulingDeleteView(DeleteView):
    """Prompts users to confirm deletion of an schedule"""

    model = Scheduling
    success_url = reverse_lazy('list_schedules')


class AddEmailGroupCreateView(SuccessMessageMixin, CreateView):
    model = EmailGroup
    fields = ['Title']
    success_message = 'Group successfully created.'
    success_url = reverse_lazy('group_list')


class AddEmailGroupListView(ListView):
    """Shows users a list of schedules"""

    model = EmailGroup


class AddUsersToGroupUpdateView(SuccessMessageMixin, UpdateView):
    model = AddUser
    fields = ['first_name',  'last_name', 'email', 'phone']
    success_message = 'Group successfully updated.'


class EmailGroupDetailView(DetailView):
    """Shows users a single schedule"""

    model = EmailGroup


def emails(request):
    sendgrid_client = SendGridAPIClient(
        api_key=os.environ.get('SENDGRID_API_KEY'))
    from_email = From('admin@mookh.co.ke')
    to_email = To('james.komoh@gmail.com')
    subject = 'Testing'
    plain_text_content = PlainTextContent(
        'It works'
    )
    html_content = HtmlContent(
        '<strong>Working</strong>'
    )
    message = Mail(from_email, to_email, subject,
                   plain_text_content, html_content)
    response = sendgrid_client.send(message=message)

    return HttpResponse('Email Sent!')


class SendUserEmails(FormView):
    template_name = 'automation/send_email.html'
    form_class = SendEmailForm
    success_message  = 'Email Sent'
    success_url = reverse_lazy('group_list')
    
    def form_valid(self, form):
        sendgrid_client = SendGridAPIClient(
        api_key=os.environ.get('SENDGRID_API_KEY'))
        from_email = From('admin@mookh.co.ke')
        to_email = form.cleaned_data['users']
        subject = form.cleaned_data['subject']
        plain_text_content = PlainTextContent(
            'It works'
        )
        text = form.cleaned_data['message']
        message = Mail(from_email, to_email, subject, plain_text_content, text)
        response = sendgrid_client.send(message=message)

        return super(SendUserEmails, self).form_valid(form)

# EMAILS SCHEDULING
class EmailSchedulingCreateView(SuccessMessageMixin, CreateView):
    """Powers a form to create a new schedule"""

    model = SchedulingEmails
    fields = ['name', 'email', 'time', 'time_zone']
    success_message = 'Email Schedule successfully created.'
    success_url = reverse_lazy('list_schedules')