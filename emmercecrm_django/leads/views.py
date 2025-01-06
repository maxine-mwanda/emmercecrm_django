from rest_framework import viewsets
from .models import Lead, Contact, Note, Reminder
from .serializers import LeadSerializer, ContactSerializer, NoteSerializer, ReminderSerializer
from .tasks import send_reminder

class LeadViewSet(viewsets.ModelViewSet):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer

class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

class ReminderViewSet(viewsets.ModelViewSet):
    queryset = Reminder.objects.all()
    serializer_class = ReminderSerializer

    def perform_create(self, serializer):
        reminder = serializer.save()
        send_reminder.apply_async((reminder.id,), eta=reminder.schedule_at)
