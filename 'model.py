from django.db import models

class Book:
    def __init__(self, title, author, total_copies):
        self.title = title
        self.author = author
        self.total_copies = total_copies
        self.available_copies = total_copies

class Reader:
    def __init__(self, name):
        self.name = name

class Reservation:
    def __init__(self, book, reader):
        self.book = book
        self.reader = reader
        self.reserved_date = None
        self.return_date = None
        self.overdue_penalty = 0