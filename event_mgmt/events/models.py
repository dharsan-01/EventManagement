from django.db import models

class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=200)
    organizer = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Attendee(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    attendee_name = models.CharField(max_length=100)
    attendee_email = models.EmailField()
    attendee_phone = models.CharField(max_length=15)


    def __str__(self):
        return f"{self.name} ({self.event.title})"
