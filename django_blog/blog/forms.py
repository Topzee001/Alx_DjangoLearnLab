from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django.forms import EmailField, CharField
from django.utils.translation import gettext_lazy as _
from django.db import models
from django.core.exceptions import ValidationError
from django import forms
from .models import Profile, Post

class CustomUserCreationForm(UserCreationForm):
    email = EmailField(label=_("Email address"), required=True, help_text=_("Required."))
    first_name = CharField(label=_("First name"), max_length=150, required=False)  # Optional, but you can set required=True
    last_name = CharField(label=_("Last name"), max_length=150, required=False)

    class Meta:
        model = User
        fields = ("username","first_name", "last_name", "email", "password1", "password2")
    
    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise ValidationError(_("This email address is already in use. Please use a different email."))
        return email

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

    def clean_email(self):
        email = self.cleaned_data.get("email")
        # Check if email is taken by another user (exclude current user)
        if User.objects.filter(email=email).exclude(pk=self.instance.pk).exists():
            raise ValidationError(_("This email address is already in use. Please use a different email."))
        return email
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields.pop('password', None)

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ("bio", "profile_picture")

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("title", "content") # fields available for aditing in the form, other fields in the model are auto generated
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}), # Add CSS class for styling
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows':6}) # Textarea for content
        }
        labels = {
            'title':_('Title'),
            'content':_('Content'),
        }
        help_texts = {
            'title': _('Enter a catchy title for your post.'),
            'content': _('Write your Blog post here'),
        }
    # custom validation (e.g., ensure title isn't empty, though Meta required handles it (optional)
    def clean_title(self):
        title = self.cleaned_data.get('title')
        if not title:
            raise forms.ValidationError(_('Title cannot be empty'))
        return title
    
