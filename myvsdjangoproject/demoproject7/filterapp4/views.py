from django.shortcuts import render
from datetime import date
# Create your views here.

def showDate(request):
    courses = ['Django', 'Python', 'Java', 'Adv Java']
    # courses = []
    return render(request, 'filterapp4/show1.html', {'courses':courses})

# def showDate(request):
#     b_day = date(1978, 12, 22)
#     myself = {'name':'Sachin','age':42, 'birthday':b_day}
#     return render(request, 'filterapp4/show2.html', {'myself':myself})
