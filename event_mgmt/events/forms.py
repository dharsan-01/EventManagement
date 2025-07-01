from django import forms
from .models import Event, Attendee

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = '__all__'

class AttendeeForm(forms.ModelForm):
    class Meta:
        model = Attendee
        fields = ['event', 'attendee_name', 'attendee_email', 'attendee_phone'] 
