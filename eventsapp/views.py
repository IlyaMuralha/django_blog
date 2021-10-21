from django.shortcuts import render


def home(request):
    return render(request, 'eventsapp/home.html')
