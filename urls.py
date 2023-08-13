
from django.urls import path
from . import views

urlpatterns = [
     path('books/', views.book_list, name='book_list'),
    path('reserve/<int:book_id>/', views.reserve_book, name='reserve_book'),
]