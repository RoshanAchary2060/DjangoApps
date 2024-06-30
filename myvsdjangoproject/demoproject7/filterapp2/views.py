from django.shortcuts import render
from datetime import datetime
# Create your views here.

# def showDate(request):
#     myname = 'Sachin'
#     return render(request, 'filterapp2/show1.html', {'name':myname})

def showDate(request):
    age = 5
    return render(request, 'filterapp2/show2.html', {'age':age})
