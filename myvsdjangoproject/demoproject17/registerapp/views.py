from django.shortcuts import render
from registerapp import forms

# def showRegistrationform(request):
#     if request.method == 'POST':
#         regform = forms.RegisterForm(request.POST)
#         print('is valid called')
#         if regform.is_valid():
#             print('Validation successful...')
#             name = regform.cleaned_data['name']
#             gr_year = regform.cleaned_data['gr_year']
#             dob = regform.cleaned_data['dob']
#             gender = regform.cleaned_data['gender']
#             print('Name:',name)
#             print('Graduation year:',gr_year)
#             print('dob:', dob,' Type:', type(dob))
#             print('gender:', gender)
#         else:
#             print('Validation failed')
#     else:
#         regform = forms.RegisterForm()
#     return render(request, 'registerapp/showregform.html', {'regform':regform})

def showRegistrationform(request):
    if request.method == "POST":
        regform = forms.RegisterForm(request.POST)
        if regform.is_valid():
            print('Validation Successful...')
            name = regform.cleaned_data['name']
            gr_year = regform.cleaned_data['gr_year']
            dob = regform.cleaned_data['dob']
            gender = regform.cleaned_data['gender']
            print('Name:',name)
            print('Graduation year:',gr_year)
            print('dob:', dob,' Type:', type(dob))
            print('gender:', gender)
        else:
            print('Validation failed')
    else:
        print('request is get')
        regform = forms.RegisterForm()
    return render(request, 'registerapp/showregform.html', {'regform':regform})
    