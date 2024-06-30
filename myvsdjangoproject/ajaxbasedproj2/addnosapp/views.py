from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponse

def home(request):
    return render(request, 'addnosapp/home.html')

def addnos(request):
    a = int(request.GET['firstnum'])
    b = int(request.GET['secnum'])
    c = a + b
    return HttpResponse(f'Sum is {c}')
