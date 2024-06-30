from django.shortcuts import render
from datetime import datetime

# Create your views here.

# def showDate(request):
#     str = 'sAChin kApoor'
#     return render(request, 'filterapp1/show1.html', {'name':str})

# def showDate(request):
#     names = ['Sachin', 'Ravi', 'Sumit']
#     return render(request,'filterapp1/show2.html', {'allnames':names})

# def showDate(request):
#     currDate = datetime.now()
#     return render(request, 'filterapp1/show3.html', {'today':currDate})

# def showDate(request):
#     # account = 'angelpriya'
#     account = ''
#     return render(request, 'filterapp1/show4.html', {'username':account})
#     even if we did not pass dictionary, no error

def showDate(request):
    # age = "25" it is also okay
    age = 25
    return render(request, 'filterapp1/show5.html', {'age':age})
