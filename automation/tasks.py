from __future__ import absolute_import

import arrow
import dramatiq

from django.conf import settings
from twilio.rest import Client

from .models import Scheduling


# Uses credentials from the TWILIO_ACCOUNT_SID and TWILIO_AUTH_TOKEN
# environment variables
client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)


@dramatiq.actor
def send_sms_reminder(schedule_id):
    """Send a reminder to a phone using Twilio SMS"""
    # Get our schedule from the database
    try:
        schedule = Scheduling.objects.get(pk=schedule_id)
    except Schedule.DoesNotExist:
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
