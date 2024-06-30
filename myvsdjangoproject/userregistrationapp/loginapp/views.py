from django.shortcuts import render
from loginapp import forms
from registerapp import models
def showLoginForm(request):
    context={}
    if request.method == 'POST':
       logform = forms.UserLoginForm(request.POST)
       if logform.is_valid():
          uid = logform.cleaned_data["userid"]
          pwd=logform.cleaned_data["password"]
          print('userid:', uid)
          print('password:', pwd)
          userobj = logform.save(commit=False) # it only gives model object but doesnot save on database
          print('userobj:', userobj)
          dbuser = models.UserModel.objects.filter(userid=uid, password=pwd)
                                        # using get() is not good as it might give exception
          if len(dbuser) == 0: # dbuser is QuerySet
             context['failed'] = 'failed'
             logform = forms.UserLoginForm()
          else:
             context['username'] = dbuser[0].username
             request.session['logged_in'] = True
             return render(request,'loginapp/secretpage.html',context)
          
    else:
        logform = forms.UserLoginForm()
    
    context['form']=logform
    return render(request,'loginapp/showloginform.html',context)
def logout(request):
    context={}
    try:
        del request.session['logged_in'] # deleting dictionary key
    except KeyError:
        logform = forms.UserLoginForm()
        context['form']=logform
        return render(request,'loginapp/showloginform.html',context)
    return render(request, 'loginapp/showlogout.html')