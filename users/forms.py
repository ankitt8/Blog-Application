from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def clean(self):
        cd = self.cleaned_data

        email = cd.get("email")
        uname = cd.get("username")
        temp = User.objects.all()
        for usr in temp:
            if usr.username == uname:
                raise forms.ValidationError("UserName already in use")

        for usr in temp:
            if usr.email == email:
                raise forms.ValidationError("Email already in use")
        return cd


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
