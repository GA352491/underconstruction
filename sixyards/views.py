from django.shortcuts import render, redirect
from .models import Event, Emails
import datetime


# Create your views here.

def home(request):
    event = Event.objects.first()
    today = datetime.datetime.now()

    if request.method == 'POST':
        mail = request.POST.get('email')
        Emails.objects.create(mails=mail)
    context = {'event': event, 'today': today}
    return render(request, 'home.html', context)


def error_404_view(request, exception):
    return redirect('home')
