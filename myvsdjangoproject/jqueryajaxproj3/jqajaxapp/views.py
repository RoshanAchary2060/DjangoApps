from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponse

def home(request):
    return render(request, 'jqajaxapp/home.html')

def getdate(request):
    currdatetime = datetime.now()
    currdate = currdatetime.strftime('%d-%b-%Y')
    currtime = currdatetime.strftime('%H:%M:%S')
    text = f'Current date is {currdate}<b>'
    text2 = f' {text} <h3 id="time">Current time is {currtime}</h3>'
    return HttpResponse(text2)
