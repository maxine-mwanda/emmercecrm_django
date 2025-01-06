from celery import shared_task
from django.core.mail import send_mail
from .models import Reminder

@shared_task
def send_reminder_email(reminder_id):
    """
    Task to send an email reminder for a specific lead.
    """
    try:
        reminder = Reminder.objects.get(id=reminder_id)
        lead = reminder.lead

        # Example: Sending email
        send_mail(
            subject=f"Reminder: {reminder.title}",
            message=f"Hi {lead.name},\n\nThis is a reminder for: {reminder.title}.\n\nThanks!",
            from_email='your_email@example.com',
            recipient_list=[lead.email],
        )
        return f"Reminder email sent to {lead.email} for reminder ID {reminder_id}"
    except Reminder.DoesNotExist:
        return f"Reminder ID {reminder_id} not found."
