from django import forms
from . import models
# class RegisterForm(forms.ModelForm):
#     password = forms.CharField(widget=forms.PasswordInput,
#                 max_length=8)
# It's priority is greater

#     class Meta:
#         model = models.RegisterModel
#         # fields = '__all__'
#         fields = ['userid','password','username']
#         labels = {'userid':'Enter userid',
#                   'password':'Enter password',
#                   'username':'Enter username'}
#         error_messages = {
#             'userid':{'required':'Userid compulsory!'},
#             'password':{'required':'Password compulsory!'},
#             'username':{'required':'Username compulsory!'}
#         }
#         widgets = {#'password':forms.PasswordInput(attrs={'placeholder':'Enter password'}),
#                    'userid':forms.TextInput(attrs={'placeholder':'Enter userid'}),
#                    'username':forms.TextInput(attrs={'placeholder':'Enter username'})}
        
class RegisterForm(forms.ModelForm):
    class Meta:
        model = models.RegisterModel
        # fields = "__all__"
        fields = ['userid','password','username']
        labels = {'userid':'Enter userid',
                  'password':'Enter pasword',
                  'username':'Enter username'}
        widgets = {'password':forms.PasswordInput(attrs={'placeholder':'Enter password'}),
                   'userid':forms.TextInput(attrs={'placeholder':'Enter userid'}),
                   'username':forms.TextInput(attrs={'placeholder':'Enter username'})}
        error_messages = {'userid':{'required':'Userid compulsory!'},
                          'password':{'required':'Password compulsory!'},
                          'username':{'required':'Username compulsory!'}}