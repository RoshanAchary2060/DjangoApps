from django import forms
from datetime import date

# class RegisterForm(forms.Form):
#     name = forms.CharField(label='Your Name', min_length=5, max_length=10)
#     gr_year = forms.IntegerField(label='Gr. Year', min_value=2020)
#     dob = forms.DateField(widget=forms.SelectDateWidget(years=range(1990,date.today().year)))
#     gender = forms.ChoiceField(choices=[(' ','Choose'),('M','Male'),('F','Female')])

class RegisterForm(forms.Form):
    name = forms.CharField(min_length=5, max_length=10, label='Your Name')
    gr_year = forms.IntegerField(min_value=2000, label='Gr. Year')
    dob = forms.DateField(widget=forms.SelectDateWidget(years=range(1990,date.today().year+1)))
    gender = forms.ChoiceField(choices=[(' ','Choose'), ('M','Male'),('F','Female')])


    def clean_dob(self):
        print('clean dob called')
        dob = self.cleaned_data['dob']
        curryear = date.today().year
        if curryear - dob.year < 18 :
            raise forms.ValidationError('You are underaged!')
        return dob

    # def clean_dob(self):
    #     print('clean dob called')
    #     dob = self.cleaned_data["dob"]
    #     curryear = date.today().year
    #     if curryear - dob.year < 18:
    #         raise forms.ValidationError('You are underaged!')
    #     return dob
    
    # these functions have 4 tasks
    # - to access data from cleaned_data dictionary
    # - to validate that data using own validations
    # - if validation fails then generate validation error
    # - lastly return that data, also we can make changes to that data,
    # - django copies that data to the cleaned_data dictionary thinking that we have made changes to that data
    
    def clean_gender(self):
        print('clean_gender() called')
        gender = self.cleaned_data.get('gender')
        if gender!= 'M' and gender != 'F':
            raise forms.ValidationError('Please select gender!')
        return gender
    
    # these are validation functions for individual fields

    # this function is for combined validation in multiple fields
    # def clean(self):
    #     print('single clean called')
    #     dob = self.cleaned_data['dob']
    #     curryear = date.today().year
    #     if curryear - dob.year < 18 :
    #         raise forms.ValidationError('You are underaged!')
    #     print('it reached here')
    #     gender = self.cleaned_data.get('gender')
    #     if gender!= 'M' and gender != 'F':
    #         raise forms.ValidationError('Please select gender...')
    #     return self.cleaned_data

    # this is only good for combined validation fields
    # if it finds error at once then it doesnot run the rest of the code
    # so we cannot validate multiple individual fields by this method