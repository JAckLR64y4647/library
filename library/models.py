from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    total_copies = models.PositiveIntegerField()
    available_copies = models.PositiveIntegerField()

    def __str__(self):
        return self.title

class Reader(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name

class Reservation(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    reader = models.ForeignKey(Reader, on_delete=models.CASCADE)
    reserved_date = models.DateTimeField(auto_now_add=True)
    return_date = models.DateTimeField()
    penalty = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)

    def __str__(self):
        return f"{self.book} reserved by {self.reader}"