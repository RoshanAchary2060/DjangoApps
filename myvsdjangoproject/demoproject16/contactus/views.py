from urllib import response
from django.http import HttpResponseRedirect
from django.shortcuts import render
from contactus import forms
# Create your views here.

def showContactForm(request):
    if request.method == 'POST':
        print('Request is post')
        myform = forms.ContactForm(request.POST)
        # print(myform)
        if myform.is_valid():
            print('Validation pass')
            print('Name:', myform.cleaned_data['name'])
            print('Email:',myform.cleaned_data['email'])
            print('Password:',myform.cleaned_data['password'])
            print('Message:',myform.cleaned_data['message'])
            username = myform.cleaned_data['name']
            # return HttpResponseRedirect('/contact/thankyou') # we cannot pass data
            return render(request, 'contactus/thankyou.html', {"username":username})
        else:
            print('Validation fail')
    else:
        print('Request is get')
        myform = forms.ContactForm()
        # print(myform)
    return render(request, 'contactus/showcontactform.html',{'form':myform})

# def showContactForm(request):
    # if request.method == 'POST':
    #     print('Request is post')
    #     myform = forms.ContactForm(request.POST) # this will create a form with data
                                                   # but password field will be empty
    #     # print(myform) 
    #     if myform.is_valid():
    #         print("Validation pass")
    #         print('Name:',myform.cleaned_data['name'])
    #         print('Email:',myform.cleaned_data['email'])
    #         print('Password:', myform.cleaned_data['password'])
    #         print('Message:', myform.cleaned_data['message'])
    #         # username = {'username':myform.cleaned_data['name']}
    #         # return render(request, 'contactus/thankyou.html', username)
    #         return HttpResponseRedirect('/contact/thankyou')
    #     else:
    #         print("Validation fail")
    # else:
    #     print('Request is get')
    #     myform = forms.ContactForm() # this will create a blank form
    # return render(request, 'contactus/showContactForm.html', {'form':myform})

def showThankyouPage(request):
    return render(request, 'contactus/thankyou.html')
