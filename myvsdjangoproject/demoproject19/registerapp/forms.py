from django import forms

class RegisterForm(forms.Form):
    # name = forms.CharField(validators=[validators.MaxLengthValidator(10)])
    # name = forms.CharField(max_length=30,error_messages={'required':'Please enter your name'})
    # email = forms.EmailField(max_length=20, error_messages={'required':'Please enter your email', 'invalid':'Not a valid email!'})
    name = forms.CharField(max_length=20, error_messages={'required':'Please enter your name!'})
    email = forms.EmailField(max_length=20,error_messages={'required':'Please enter your email!','invalid':'Not a valid email!'})