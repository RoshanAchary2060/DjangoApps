from django.shortcuts import render
from datetime import datetime, date
# Create your views here.

# def showDate(request):
#     b_day = date(1978, 12, 22)
#     myself = {'name':"Sachin", "age":42, "birthday":b_day}
#     return render(request, 'filterapp3/show1.html', {'myself':myself})

# def showDate(request):
#     text = "Django Rocks!"
#     return render(request, 'filterapp3/show2.html', {'message':text})

def showDate(request):
    courses = ['Django', 'Python', 'Java', 'Adv Java']
    return render(request, 'filterapp3/show3.html', {'courses':courses})
