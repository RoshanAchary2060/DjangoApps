from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponse
# Create your views here.

def showDateTime(request):
    today = datetime.now()
    currDT = today.strftime('%d-%b-%Y, %I:%M:%S %p')
    text = f"<h2>Current date and time at the server is {currDT}</h2>"
    return HttpResponse(text)
