from django import forms
from .models import Book

class BookReservationForm(forms.Form):
    book_id = forms.IntegerField(widget=forms.HiddenInput())
    user_name = forms.CharField(max_length=255)
    pickup_date = forms.DateField()