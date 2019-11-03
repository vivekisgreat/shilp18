from django.contrib.auth.models import User
from django import forms
from .models import Profiles

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    name = forms.CharField(max_length=100)
    email = forms.EmailField(required = True)
    mobile_no = forms.CharField(max_length=10)
    residential_address = forms.CharField(max_length=300)
    college_name = forms.CharField(max_length=300)
    year = forms.ChoiceField(choices = [(None,'Select'),('I','I'),('II','II'),('III','III'),('IV','IV'),('V','V')])

    class Meta:
        model = User
        fields = ['username','password','name','password','email','mobile_no','residential_address','college_name','year']

