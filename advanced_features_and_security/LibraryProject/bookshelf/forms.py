# LibraryProject/bookshelf/forms.py

from django import forms
from .models import Book

class ExampleForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author']
        labels = {
            'title': 'Book Title',
            'author': 'Author',
        }
