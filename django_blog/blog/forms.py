from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django.forms import EmailField, CharField
from django.utils.translation import gettext_lazy as _
from django.db import models
from django import forms
from .models import Profile

class CustomUserCreationForm(UserCreationForm):
    email = EmailField(label=_("Email address"), required=True, help_text=_("Required."))
    first_name = CharField(label=_("First name"), max_length=150, required=False)  # Optional, but you can set required=True
    last_name = CharField(label=_("Last name"), max_length=150, required=False)

    class Meta:
        model = User
        fields = ("username","first_name", "last_name", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.email= self.cleaned_data["email"]
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data['last_name']
        if commit:
            user.save()
        return user
    
class ProfileUpdateForm(UserChangeForm):

    class Meta:
        model = User
        fields = ("username", "email", "first_name", "last_name")
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields.pop('password', None)

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ("bio", "profile_picture")