from django import forms
from django.contrib.auth.forms import UserCreationForm
from bookshelf.models import CustomUser
from .models import Book

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'email', 'date_of_birth')

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author']