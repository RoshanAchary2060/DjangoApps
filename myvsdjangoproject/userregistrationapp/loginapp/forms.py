from django import forms
from registerapp import models
class UserLoginForm(forms.ModelForm):
      class Meta:
            model = models.UserModel
            fields=['userid','password']
            labels = {'userid': 'Enter userid', 'password': 'Enter password'}
            error_messages = {
                'userid': {'required': 'Id required!'},
                'password': {'required': 'Password required!'},
               
                }
            widgets = {

                'password': forms.PasswordInput(attrs={'placeholder': 'Type password'}),
                'userid': forms.TextInput(attrs={'placeholder': 'Type userid'})
                }
            