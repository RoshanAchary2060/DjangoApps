from django.shortcuts import render
from registerapp import forms

def showRegistrationForm(request):
    context={}
    if request.method == 'POST':
       regform = forms.UserRegisterForm(request.POST)
       if regform.is_valid():
          uid = regform.cleaned_data["userid"]
          pwd=regform.cleaned_data["password"]
          uname = regform.cleaned_data['username']
          print('userid:', uid)
          print('password:', pwd)
          print('username:', uname)
          userobj = regform.save() # userobj is model object
          print('userobj:', userobj)
          regform=forms.UserRegisterForm()
          context['success'] = 'success'
          context['username']=userobj.username              
    else:
        regform = forms.UserRegisterForm()
    context['form']=regform
    return render(request,'registerapp/showregform.html',context)
