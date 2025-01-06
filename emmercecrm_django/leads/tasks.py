from celery import shared_task
from .models import Reminder

def send_email(subject, message, recipient):
    # Mock email sending function
    print(f"Email sent to {recipient}: {subject}\n{message}")

@shared_task
def send_reminder(reminder_id):
    try:
        reminder = Reminder.objects.get(id=reminder_id)
        send_email(
            subject="Reminder",
            message=reminder.message,
            recipient=reminder.lead.email
        )
    except Reminder.DoesNotExist:
        print(f"Reminder with ID {reminder_id} does not exist.")
