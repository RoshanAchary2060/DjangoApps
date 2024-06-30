from django.shortcuts import render
from registerapp import forms, models

def showRegistrationform(request):
    context = {}
    if request.method == 'POST':
        regform = forms.RegisterForm(request.POST)
        print('is valid called')
        if regform.is_valid():
            obj = regform.save()
            regform = forms.RegisterForm()
            context['success']='done'
            context['username']=obj.username
        else:
            print('Validation failed')
    else:
        regform = forms.RegisterForm()
    context['regform']= regform
    return render(request, 'registerapp/showregform.html',context)
