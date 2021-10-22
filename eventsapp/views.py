from django.shortcuts import render
from .models import Event


def home(request):
    events = Event.objects
    return render(request, 'eventsapp/home.html', {'events': events})
