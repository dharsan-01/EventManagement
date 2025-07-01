from django.shortcuts import render

from django.shortcuts import render, redirect, get_object_or_404
from .models import Event, Attendee
from .forms import EventForm, AttendeeForm

# Event Views
def event_list(request):
    events = Event.objects.all()
    return render(request, 'events/event_list.html', {'events': events})

def event_detail(request, pk):
    event = get_object_or_404(Event, pk=pk)
    return render(request, 'events/event_detail.html', {'event': event})

def create_event(request):
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('event_list')
    else:
        form = EventForm()
    return render(request, 'events/create_event.html', {'form': form})

def update_event(request, pk):
    event = get_object_or_404(Event, pk=pk)
    form = EventForm(request.POST or None, instance=event)
    if form.is_valid():
        form.save()
        return redirect('event_list')
    return render(request, 'events/update_event.html', {'form': form})

def delete_event(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if request.method == "POST":
        event.delete()
        return redirect('event_list')
    return render(request, 'events/delete_event.html', {'event': event})

# Attendee Views
def attendee_list(request):
    attendees = Attendee.objects.all()
    return render(request, 'events/attendee_list.html', {'attendees': attendees})

def create_attendee(request):
    if request.method == "POST":
        form = AttendeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('attendee_list')
    else:
        form = AttendeeForm()
    return render(request, 'events/create_attendee.html', {'form': form})

def delete_attendee(request, pk):
    attendee = get_object_or_404(Attendee, pk=pk)
    if request.method == "POST":
        attendee.delete()
        return redirect('attendee_list')
    return render(request, 'events/delete_attendee.html', {'attendee': attendee})
