from django.db import models
from django.utils import timezone

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    published_date = models.DateField()
    isbn = models.CharField(max_length=13, unique=True)

    def __str__(self):
        return self.title


class Member(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    joined_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class Borrow(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrow_date = models.DateTimeField(default=timezone.now)
    return_date = models.DateTimeField(null=True, blank=True)

    def is_returned(self):
        return self.return_date is not None

    def return_book(self):
        """Mark this borrowed book as returned"""
        self.return_date = timezone.now()
        self.save()

    def __str__(self):
        status = "Returned" if self.is_returned() else "Borrowed"
        return f"{self.member.name} - {self.book.title} ({status})"
