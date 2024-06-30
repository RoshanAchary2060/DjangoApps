from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponse
# Create your views here.

def showDate(request):
    today = datetime.now()
    currDate = today.strftime('%d-%b-%Y')
    text = f"<h2> Current date is {currDate}</h2>"
    return HttpResponse(text)

def showTime(request):
    today = datetime.now()
    currTime = today.strftime('%I:%M:%S %p')
    text = f"<h2> Current time is {currTime}</h2>"
    return HttpResponse(text)
