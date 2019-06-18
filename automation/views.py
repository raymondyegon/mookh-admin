from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import DeleteView
from django.views.generic.edit import UpdateView
from django.views.generic.list import ListView
from django.shortcuts import render


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


from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives

def sendEmail(request):
    mail = EmailMultiAlternatives(
    subject="Email Test",
    body="This is a simple text email body.",
    from_email="K.O.M.O <james.komoh@gmail.com>",
    to=["juniorgichohi@gmail.com"],
    headers={"Reply-To": "juniorgichohi@gmail.com"}
    )
    # Add template
    # mail.template_id = 'YOUR TEMPLATE ID FROM SENDGRID ADMIN'

    # Replace substitutions in sendgrid template
    mail.substitutions = {'%username%': 'komo'}

    # Attach file
    with open('emailTest.pdf', 'rb') as file:
        mail.attachments = [
            ('emailTest.pdf', file.read(), 'application/pdf')
        ]

    mail.attach_alternative(
        "<p>This is a simple HTML email body</p>", "text/html"
    )

    mail.send()
    return render(request, 'appointments/send-email/emailsent.html')

# # sending email
# def send_email(request):

#     all_users = User.objects.all()
#     subject ='Newsletter'
#     from_email = settings.DEFAULT_FROM_EMAIL

#     # newsletter content below. can also entered via txt file or html file
#     content_message = 'Newsletter content <a href="https://programmedtocode.wordpress.com/>CLICK LINK</a>"'
#     for user_email in all_users:
#         """
#         to_email = [user_email.email]
#         context = {
#         'email' : from_email,
#         'message' : content_message,
#         }
#         final_send_content = get_template('Newsletter_content.txt').render(context)
#         """

#         if user_email.username == 'owner':  # to ignore superuser 'owner' 
#             continue
#         else:
#             to_email = user_email.email
#             send_mail(subject,content_message,from_email, [to_email], fail_silently=True)

#     return HttpResponse("mail sent")