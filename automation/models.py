from __future__ import unicode_literals

import redis

from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse
from django.utils.encoding import python_2_unicode_compatible
from timezone_field import TimeZoneField

import arrow

# Create your models here.
class Scheduling(models.Model):
    name = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=15)
    time = models.DateTimeField()
    time_zone = TimeZoneField(default='Africa/Nairobi')

    # Additional fields not visible to users
    task_id = models.CharField(max_length=50, blank=True, editable=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'Scheduling #{0} - {1}'.format(self.pk, self.name)

    def get_absolute_url(self):
        return reverse('view_schedules', args=[str(self.id)])

    def clean(self):
        """Checks that appointments are not scheduled in the past"""

        schedule_time = arrow.get(self.time, self.time_zone.zone)

        if schedule_time < arrow.utcnow():
            raise ValidationError(
                'You cannot schedule an appointment for the past. '
                'Please check your time and time_zone')

    def schedule_reminder(self):
            """Schedule a Dramatiq task to send a reminder for this schedule"""

            # Calculate the correct time to send this reminder
            schedule_time = arrow.get(self.time, self.time_zone.zone)
            reminder_time = schedule_time.shift(minutes=-30)
            now = arrow.now(self.time_zone.zone)
            milli_to_wait = int(
                (reminder_time - now).total_seconds()) * 1000

            # Schedule the Dramatiq task
            from .tasks import send_sms_reminder
            result = send_sms_reminder.send_with_options(
                args=(self.pk,),
                delay=milli_to_wait)

            return result.options['redis_message_id']

    def save(self, *args, **kwargs):
        """Custom save method which also schedules a reminder"""

        # Check if we have scheduled a reminder for this schedule before
        if self.task_id:
            # Revoke that task in case its time has changed
            self.cancel_task()

        # Save our schedule, which populates self.pk,
        # which is used in schedule_reminder
        super(Scheduling, self).save(*args, **kwargs)

        # Schedule a new reminder task for this appointment
        self.task_id = self.schedule_reminder()

        # Save our schedule again, with the new task_id
        super(Scheduling, self).save(*args, **kwargs)

    def cancel_task(self):
        redis_client = redis.Redis(host='localhost', port=6379, db=0)
        redis_client.hdel("dramatiq:default.DQ.msgs", self.task_id)
