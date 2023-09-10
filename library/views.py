from django.shortcuts import render, get_object_or_404, redirect
from .models import Book, Author
from .forms import BookReservationForm

def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})

def reserve_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    if request.method == 'POST':
        form = BookReservationForm(request.POST)
        if form.is_valid():
            user_name = form.cleaned_data['user_name']
            pickup_date = form.cleaned_data['pickup_date']
            if book.reserved_copies < book.available_copies:
                book.reserved_copies += 1
                book.save()
                return redirect('book-list')
    else:
        form = BookReservationForm(initial={'book_id': book_id})
    
    return render(request, 'reserve_book.html', {'form': form, 'book': book})

def check_book_status(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    if book.reserved_copies < book.available_copies:
        status_message = 'Книгу можна взяти'
    else:
        status_message = 'Книгу зараз неможливо взяти, всі копії зарезервовані'
    return render(request, 'book_status.html', {'book': book, 'status_message': status_message})