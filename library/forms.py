from django import forms
from .models import Book, Reader

class BookReservationForm(forms.Form):
    book = forms.ModelChoiceField(queryset=Book.objects.filter(available_copies__gt=0))
    reader = forms.ModelChoiceField(queryset=Reader.objects.all())
    return_date = forms.DateTimeField(widget=forms.TextInput(attrs={'placeholder': 'YYYY-MM-DD HH:MM'}))

class BookReturnForm(forms.Form):
    book = forms.ModelChoiceField(queryset=Book.objects.filter(reservation__isnull=False))
    return_date = forms.DateTimeField(widget=forms.TextInput(attrs={'placeholder': 'YYYY-MM-DD HH:MM'}))
