from django.urls import path
from .views import BookListView, reserve_book, return_book

urlpatterns = [
    path('', BookListView.as_view(), name='book_list'),
    path('reserve/', reserve_book, name='reserve_book'),
    path('return/', return_book, name='return_book'),
]
