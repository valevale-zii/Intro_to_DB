from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from .models import Borrow, Book

def return_book(request, borrow_id):
    borrow = get_object_or_404(Borrow, id=borrow_id)

    if not borrow.is_returned():  
        borrow.return_date = timezone.now()  
        borrow.save()
        
        # Optional: increase available copies of the book
        book = borrow.book
        book.available_copies += 1
        book.save()

    return redirect('borrow_list')  # Change to the page you want after return
