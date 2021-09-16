from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import User
from App_Login.models import UserProfile


class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="Email address", required=True)
    # first_name= forms.CharField(label="First Name", required=True)
    # last_name= forms.CharField(label="Last Name", required=True)
    class Meta:
        model = User
        fields =('username','email','password1','password2')

class UserProfileChange(UserChangeForm):
    class Meta:
        model = User
        fields = ('username','email','first_name','last_name','password')

class ProfilePic(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['profile_pic',]
