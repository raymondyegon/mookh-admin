from django.db import models
from timezone_field import TimeZoneField
from django.urls import reverse

# Create your models here.
class Scheduling(models.Model):
    name = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=15)
    time = models.DateTimeField()
    time_zone = TimeZoneField(default='UTC')

    # Additional fields not visible to users
    task_id = models.CharField(max_length=50, blank=True, editable=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'Scheduling #{0} - {1}'.format(self.pk, self.name)

    def get_absolute_url(self):
        return reverse('view_schedules', args=[str(self.id)])

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