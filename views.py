from django.shortcuts import render, redirect
from .models import Book, Reader, Reservation

books = []
readers = []
reservations = []

def book_list(request):
    return render(request, 'book_list.html', {'books': books})

def reserve_book(request, book_id):
    book = books[book_id]
    if book.available_copies > 0:
        reader, created = Reader.objects.get_or_create(name="Anonymous Reader")
        if not created:
            pass

        reservation, created = Reservation.objects.get_or_create(book=book, reader=reader, return_date=None)
        if not created:
            pass

        book.available_copies -= 1

    return redirect('book_list')