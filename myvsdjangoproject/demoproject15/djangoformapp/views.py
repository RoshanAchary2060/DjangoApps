from django.shortcuts import render

from djangoformapp import forms

def showForm(request):
    # values = {'username': 'Your name', 'useremail':'Your email'}
    # fobj = forms.EmpRegistration(auto_id=False,label_suffix='okay', initial=values)
    fobj = forms.EmpRegistration(initial={'username':'Roshan'})
    # print('Form is bounded:', fobj.is_bound)
    fobj.order_fields(field_order=['useremail', 'username'])
    # wrong field names are simply ignored
    return render(request, 'djangoformapp/showform.html', {'regform':fobj})
