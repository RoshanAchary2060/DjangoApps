from django.shortcuts import render
from registerapp import forms, models

def showRegistrationform(request):
    context = {}
    if request.method == 'POST':
        regform = forms.RegisterForm(request.POST)
        print('is valid called')
        if regform.is_valid():
            print('Validation successful...')
            uid = regform.cleaned_data['userid']
            pwd = regform.cleaned_data['password']
            uname = regform.cleaned_data['username']
            print('Userid:',uid)
            print('password:',pwd)
            print('username:',uname)
            obj = models.RegisterModel(userid=uid, password=pwd,username=uname)
            obj.save()
            regform=forms.RegisterForm()
            context['success']= 'done'
            context['username']=uname
        else:
            print('Validation failed')
    else:
        regform = forms.RegisterForm()
    context['regform']= regform
    return render(request, 'registerapp/showregform.html',context)
