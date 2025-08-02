from django import forms
from .models import Book

class ExampleForm(forms.Form):
    # q is the search query
    q = forms.CharField(max_length=100, label='Search Books')

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'author', 'publication_year')