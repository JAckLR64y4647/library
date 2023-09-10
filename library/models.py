from django.db import models

class Author(models.Model):
    id = models.BigAutoField(primary_key=True) 
    name = models.CharField(max_length=255)
    birth_date = models.DateField()

    def __str__(self):
        return self.name

class Book(models.Model):
    id = models.BigAutoField(primary_key=True) 
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    available_copies = models.PositiveIntegerField()
    reserved_copies = models.PositiveIntegerField(default=0)
    penalty_rate = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)

    def __str__(self):
        return self.title