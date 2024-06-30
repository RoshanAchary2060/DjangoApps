from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponse
# Create your views here.

def showDate(request):
    today = datetime.now()
    currDate = today.strftime('%d-%b-%Y')
    text = f"<h2>Current date at the server is {currDate}</h2>"
    return HttpResponse(text)