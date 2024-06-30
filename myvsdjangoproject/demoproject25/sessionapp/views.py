from django.shortcuts import render
from . import forms
from datetime import datetime

# def showForm(request):
#     userform = forms.UserInputForm()
#     obj = datetime.today()
#     visittime = obj.strftime("%H:%M:%S")
#     request.session['visittime'] = visittime
#     return render(request, 'sessionapp/showform.html', {'form':userform})

def showForm(request):
    userform = forms.UserInputForm()
    obj = datetime.today()
    visittime = obj.strftime("%H:%M:%S")
    request.session['visittime'] = visittime
    return render(request, 'sessionapp/showform.html', {'form':userform})

# def showResponse(request):
#     context = {}
#     context['username'] = request.GET['username']
#     context['visittime']= request.session.get('visittime')
#     return render(request, 'sessionapp/response.html', context)

def showResponse(request):
    context = {}
    context['username'] = request.GET['username']
    context['visittime'] = request.session.get('visittime')
    return render(request, 'sessionapp/response.html',context)
