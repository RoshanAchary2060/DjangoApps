from django import forms

# class RegisterForm(forms.Form):
#     userid = forms.CharField(max_length=30, label='Enter userid')
#     password = forms.CharField(widget=forms.PasswordInput, label='Enter password')
#     username = forms.CharField(max_length=30, label='Enter username')

class RegisterForm(forms.Form):
    userid = forms.CharField(max_length=30,label='Enter userid')
    password = forms.CharField(widget=forms.PasswordInput,label='Enter password')
    username = forms.CharField(max_length=30,label="Enter username")
