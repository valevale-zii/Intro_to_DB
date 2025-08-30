from django.test import TestCase
from .models import Book

class BookModelTest(TestCase):
    def setUp(self):
        Book.objects.create(title="Test Book", author="Valencia", published_date="2025-01-01")

    def test_book_title(self):
        book = Book.objects.get(title="Test Book")
        self.assertEqual(book.title, "Test Book")
