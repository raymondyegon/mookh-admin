from __future__ import absolute_import

import arrow
import dramatiq

from django.conf import settings
from twilio.rest import Client

from .models import Scheduling, SchedulingEmails
from . views import *

# SEND GRID IMPORTS
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import From, To, PlainTextContent, HtmlContent, Mail
from .forms import SendEmailForm

# Uses credentials from the TWILIO_ACCOUNT_SID and TWILIO_AUTH_TOKEN
# environment variables
client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)


@dramatiq.actor
def send_sms_reminder(schedule_id):
    """Send a reminder to a phone using Twilio SMS"""
    # Get our schedule from the database
    try:
        schedule = Scheduling.objects.get(pk=schedule_id)
    except Scheduling.DoesNotExist:
        # The schedule we were trying to remind someone about
        # has been deleted, so we don't need to do anything
        return

    schedule_time = arrow.get(schedule.time, schedule.time_zone.zone)
    body = 'Hi {0}. You have an SMS schedule coming up at {1}.'.format(
        schedule.name,
        schedule_time.format('h:mm a')
    )

    client.messages.create(
        body=body,
        to=schedule.phone_number,
        from_=settings.TWILIO_NUMBER,
    )


@dramatiq.actor
def send_email_reminder(schedule_id):
    """Create an email schedule using SendGrid Emails"""
    # Get our schedule from the database
    try:
        schedule = SchedulingEmails.objects.get(pk=schedule_id)
    except SchedulingEmails.DoesNotExist:
        # The schedule we were trying to remind someone about
        # has been deleted, so we don't need to do anything
        return

    schedule_time = arrow.get(schedule.time, schedule.time_zone.zone)
    body = 'Hi {0}. You have an Meeting coming up at {1}.'.format(
        schedule.name,
        schedule_time.format('h:mm a')
    )

    # client.messages.create(
    #     body=body,
    #     to=schedule.email,
    #     from_=settings.SENDGRID_SENDER,
    # )
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
            plain_text_content = PlainTextContent('It works')
            text = form.cleaned_data['message']
            message = Mail(from_email, to_email, subject, plain_text_content, text)
            response = sendgrid_client.send(message=message)

            return super(SendUserEmails, self).form_valid(form)