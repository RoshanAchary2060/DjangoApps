from django.shortcuts import render
from registerapp import forms

def showRegistrationform(request):
    if request.method == 'POST':
        regform = forms.RegisterForm(request.POST)
        print('is valid called')
        if regform.is_valid():
            print('Validation successful...')
            name = regform.cleaned_data['name']
            email = regform.cleaned_data['email']
            print('Name:',name)
            print('Email:',email)
        else:
            print('Validation failed')
    else:
        regform = forms.RegisterForm()
    return render(request, 'registerapp/showregform.html', {'regform':regform})
