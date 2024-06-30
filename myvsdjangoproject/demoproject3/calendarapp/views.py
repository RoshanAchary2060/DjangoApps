from django.shortcuts import render
from datetime import datetime
from calendar import HTMLCalendar
from django.http import HttpResponse
# Create your views here.

def showcalendar(request):
    today = datetime.now()
    obj = HTMLCalendar()
    text = obj.formatmonth(today.year, today.month)
    return HttpResponse(text)
