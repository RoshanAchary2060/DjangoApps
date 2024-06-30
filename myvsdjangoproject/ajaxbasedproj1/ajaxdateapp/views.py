from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponse

def home(request):
    return render(request, 'ajaxdateapp/home.html')

def getdate(request):
    currdatetime = datetime.now()
    currdate = currdatetime.strftime("%d-%b-%Y")
    text = f'Current date is {currdate}'
    return HttpResponse("<h2>" + text + "</h2>")
