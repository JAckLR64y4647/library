from django.shortcuts import render, redirect
from django.utils import timezone
from django.views.generic import ListView
from .forms import BookReservationForm, BookReturnForm
from .models import Book, Reservation

class BookListView(ListView):
    model = Book
    template_name = 'book_list.html'
    context_object_name = 'books'

def reserve_book(request):
    if request.method == 'POST':
        form = BookReservationForm(request.POST)
        if form.is_valid():
            book = form.cleaned_data['book']
            reader = form.cleaned_data['reader']
            return_date = form.cleaned_data['return_date']
            Reservation.objects.create(book=book, reader=reader, return_date=return_date)
            book.available_copies -= 1
            book.save()
            return redirect('book_list')
    else:
        form = BookReservationForm()
    return render(request, 'reserve_book.html', {'form': form})

def return_book(request):
    if request.method == 'POST':
        form = BookReturnForm(request.POST)
        if form.is_valid():
            book = form.cleaned_data['book']
            return_date = form.cleaned_data['return_date']
            reservation = Reservation.objects.get(book=book, return_date__gte=return_date)
            days_late = (timezone.now() - reservation.return_date).days
            if days_late > 0:
                reservation.penalty = days_late * 0.5
                reservation.save()
            book.available_copies += 1
            book.save()
            reservation.delete()
            return redirect('book_list')
    else:
        form = BookReturnForm()
    return render(request, 'return_book.html', {'form': form})
