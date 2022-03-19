from pyexpat import model
from django import forms
from django.contrib.auth.models import User
from .models import Profile
# Create your forms here.


# Login Form
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

# User Edit Form
class UserEditForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name')

# User Profile
class ProfileEditForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ('date_of_birth', 'photo')