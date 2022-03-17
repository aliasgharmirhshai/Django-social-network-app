from pyexpat import model
from django import forms
from django.contrib.auth.models import User
from urllib3 import Retry
# Create your forms here.


#Login Form
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class RegisterForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email') 

    def clean_pass(self):
        cd = self.cleaned_data
        # Check Password Match
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Password is Not Match')
        return cd['repeat_password']
