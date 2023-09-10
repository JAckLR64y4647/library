from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.book_list, name='book-list'),
    path('books/<int:book_id>/reserve/', views.reserve_book, name='reserve-book'),
    path('books/<int:book_id>/status/', views.check_book_status, name='book-status'),
]