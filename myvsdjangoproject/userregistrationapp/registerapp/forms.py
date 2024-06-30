from django import forms
from registerapp import models
class UserRegisterForm(forms.ModelForm):
      #password=forms.CharField(widget=forms.PasswordInput)
      class Meta:
            model = models.UserModel
            fields=['userid','password','username']
            labels = {'userid': 'Enter userid', 'password': 'Enter password', 'username': 'Enter username'}
            error_messages = {
                'userid': {'required': 'Id required!'},
                'password': {'required': 'Password required!'},
                'username': {'required': 'Name required!'}
            }
            widgets = {

                'password': forms.PasswordInput(attrs={'placeholder': 'Type password'}),
                'userid': forms.TextInput(attrs={'placeholder': 'Type userid'}),
                'username':forms.TextInput(attrs={'placeholder':'Type username'})
            }
