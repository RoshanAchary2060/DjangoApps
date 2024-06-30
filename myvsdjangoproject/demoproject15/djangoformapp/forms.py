from mimetypes import init
from django import forms

class EmpRegistration(forms.Form):
    username = forms.CharField(required=False, label='Your name') # no need of max length
    useremail = forms.EmailField(required=False,label_suffix='#',disabled=True)
    message = forms.CharField(widget=forms.Textarea, help_text='Not more than 30 characters')
    password = forms.CharField(widget=forms.PasswordInput)
    title = forms.CharField(widget = forms.Textarea) 
    description = forms.CharField(widget = forms.CheckboxInput) 
    views = forms.IntegerField(widget = forms.TextInput) 
    available = forms.BooleanField(widget = forms.Textarea) 

    # user_name = forms.CharField()
    # user_email = forms.EmailField()
    # message = forms.CharField()
