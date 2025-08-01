from django import forms
from .models import Book

class ExampleForm(forms.Form):
    # q will be used in query
    q = forms.CharField(max_length=100)


