from django import forms
from bookstore import models


class BookForm(forms.ModelForm):
    class Meta:
        model = models.Book
        fields = [
            'title',
            'author',
            'description',
            'image'
        ]


class CommentForm(forms.ModelForm):
    class Meta:
        model = models.CommentBook
        fields = [
            'book',
            'text',
        ]