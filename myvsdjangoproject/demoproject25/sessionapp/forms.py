from django import forms

# class UserInputForm(forms.Form):
#     username = forms.CharField(label='Enter your name')

class UserInputForm(forms.Form):
    username = forms.CharField(label='Enter your name')
