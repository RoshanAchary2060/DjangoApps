from django import forms
from django.core import validators

# def checkCapital(name):
#     ch = name[0]
#     if 65 <=  ord(ch) <=90:
#         return name
#     else:
#         raise forms.ValidationError("Name should begin with capital letter!")
    
def checkCapital(name):
    ch = name[0]
    if 65<= ord(ch) <= 90:
        return name
    else:
        raise forms.ValidationError("Name should begin with capital letter!")

def check_email(email):
    if '@gmail.com' in email:
        return email
    else:
        raise forms.ValidationError("email entered should be gmail id only!")


class RegisterForm(forms.Form):
    # name = forms.CharField(validators=[validators.MaxLengthValidator(10)])
    # email = forms.EmailField()
    name = forms.CharField(validators=[checkCapital])
    email = forms.EmailField(validators=[check_email])
